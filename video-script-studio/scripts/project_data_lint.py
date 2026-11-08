#!/usr/bin/env python3
"""Validate scene-image graphs, Clip mappings, object usage and delivery titles.

Uses schema_version 1 without modifying or migrating projects. Planned/null
assets are allowed. Optional video_delivery.object_usage counts distinct Clip
IDs and requires registered assets for objects used by >=2 Clips. It does not
infer identity or inventory completeness from prose. Default document coverage
is complete; --scoped allows a nonempty sample/batch subset, while supplied
registry data is always checked in full. Never validates images or bindings.
"""
from __future__ import annotations
import argparse
from collections import Counter
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import re
import sys
import director_contract_lint as contract
import seedance_lint as assets

IMAGE = re.compile(r'S\d+(?:-\d+)?\Z')
IMAGE_TOKEN = re.compile(r'(?<![\w-])S\d+(?:-\d+)?(?![\w-])')
SCENE_TITLE = re.compile(r'^#{1,6}\s+场景图\s+(S\d+(?:-\d+)?)(?=\s|[｜|]|$)')
SCOPE = re.compile(r'(?:^|[、,，\s])(?:Clip\s+)?([1-9]\d*-[1-9]\d*)'
                   r'(?:[（(]([^）)]*)[）)])?', re.I)
RANGE = re.compile(r'(\d+(?:\.\d+)?)\s*(?:s|秒)?\s*[-–—~～至]\s*'
                   r'(\d+(?:\.\d+)?)\s*(?:s|秒)?', re.I)


def number(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
        raise ValueError(f'{label} 必须是有限数值')
    result = Decimal(str(value))
    if not result.is_finite():
        raise ValueError(f'{label} 必须是有限数值')
    return result


def time_range(value, duration, label):
    if value is None:
        return (Decimal(0), duration) if duration is not None else None
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ValueError(f'{label} 必须是null或[开始秒,结束秒]')
    start, end = (number(v, label) for v in value)
    if start < 0 or end <= start or end > 30 or (duration is not None and end > duration):
        raise ValueError(f'{label} 时段非法或超出Clip时长')
    return start, end


def parse_scope(value):
    """Legacy string or structured [{clip_id,time_range_seconds}] scopes."""
    if isinstance(value, list):
        result = []
        for entry in value:
            if not isinstance(entry, dict) or not isinstance(entry.get('clip_id'), str):
                raise ValueError('结构化clip_scope条目须有clip_id')
            if not re.fullmatch(r'[1-9]\d*-[1-9]\d*', entry['clip_id']):
                raise ValueError('clip_scope中的Clip编号非法')
            result.append((entry['clip_id'], entry.get('time_range_seconds')))
        return result
    if not isinstance(value, str) or not value.strip():
        raise ValueError('clip_scope必须是非空范围字符串或数组')
    matches = list(SCOPE.finditer(value))
    residue = SCOPE.sub('', value)
    if not matches or residue.strip(' 、,，\t\r\n'):
        raise ValueError(f'无法解析clip_scope：{value}')
    result = []
    for match in matches:
        interval = match.group(2)
        if interval is None:
            result.append((match.group(1), None))
        else:
            parsed = RANGE.fullmatch(interval.strip())
            if not parsed:
                raise ValueError(f'无法解析引用时段：{interval}')
            result.append((match.group(1), [float(v) for v in parsed.groups()]))
    return result


def outside_lines(text):
    """Use the contract's fence syntax; never interpret prompt-body titles."""
    fence = None
    for line in text.splitlines():
        match = contract.FENCE.match(line)
        if match:
            marker, info = match.groups()
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not info.strip():
                fence = None
        elif fence is None:
            yield line
    if fence is not None:
        raise ValueError('代码围栏未闭合')


def image_title_refs(metadata):
    match = re.search(r'场景图\s*[:：]\s*([^\n｜|]+)', metadata)
    if not match:
        return []
    field = match.group(1).strip()
    result = []
    for item in re.split(r'[、,，]', field):
        ids = IMAGE_TOKEN.findall(item)
        if len(ids) != 1:
            raise ValueError(f'无法解析场景图标题引用：{item}')
        intervals = re.findall(r'[（(]([^）)]*)[）)]', item)
        if not intervals:
            result.append((ids[0], None))
        else:
            for interval in intervals:
                parsed = RANGE.fullmatch(interval.strip())
                if not parsed:
                    raise ValueError(f'无法解析场景图标题时段：{interval}')
                result.append((ids[0], [float(v) for v in parsed.groups()]))
    return result


def validate_object_usage(data, clips):
    """Validate an explicit inventory only; never guess identity from prose."""
    errors, warnings = [], []
    delivery = data.get('video_delivery', {})
    usage = delivery.get('object_usage')
    if 'object_usage' not in delivery:
        return [], ['未提供object_usage，资产建立门槛未核验（须人工对账）'], {
            'object_usage': 'not_provided'}
    if not isinstance(usage, list):
        return ['video_delivery.object_usage须为数组'], [], {'object_usage': 'invalid'}
    registered = {}
    for asset in data['assets']:
        if isinstance(asset, dict) and isinstance(asset.get('handle'), str):
            registered.setdefault(asset['handle'], []).append(asset)
    seen_objects, seen_handles = set(), set()
    total, shared = 0, 0
    for row in usage:
        if not isinstance(row, dict):
            errors.append('object_usage条目须为对象'); continue
        kind, name = row.get('type'), row.get('name')
        ids = row.get('clip_ids')
        if (not isinstance(kind, str) or kind not in {'C', 'B', 'P', 'S'}
                or not isinstance(name, str) or not name.strip()):
            errors.append('object_usage须有C/B/P/S类型与非空对象名'); continue
        identity = (kind, name.strip())
        if identity in seen_objects:
            errors.append(f'object_usage重复对象：{kind}/{name}'); continue
        seen_objects.add(identity)
        if not isinstance(ids, list) or any(not isinstance(v, str) for v in ids):
            errors.append(f'{name}的clip_ids须为字符串数组'); continue
        unique = set(ids)
        total += 1
        if len(unique) != len(ids):
            warnings.append(f'{name}重复Clip已按集合去重，不增加资产计数')
        unknown = unique - set(clips)
        if unknown:
            errors.append(f'{name}的object_usage引用不存在的Clip：' + '、'.join(sorted(unknown)))
        required = len(unique) >= 2
        shared += int(required)
        handle = row.get('asset_handle')
        if handle is None:
            if required:
                errors.append(f'{name}出现在{len(unique)}条独立视频提示词中，必须建立共享资产（缺asset_handle）')
            continue
        if not isinstance(handle, str) or not handle.strip():
            errors.append(f'{name}的asset_handle须为基础资产调用名或null'); continue
        if handle in seen_handles:
            errors.append(f'object_usage同一资产被拆成多行：{handle}')
        seen_handles.add(handle)
        matches = registered.get(handle, [])
        if len(matches) != 1:
            errors.append(f'{name}的共享资产未唯一登记：{handle}'); continue
        asset = matches[0]
        if asset.get('name') != name or (asset.get('type') is not None and asset['type'] != kind):
            errors.append(f'{name}的object_usage身份／类型与基础资产不一致：{handle}')
    return errors, warnings, {'object_usage': 'provided', 'usage_objects': total,
                              'shared_objects': shared}


def validate_data(data, video_text=None, scene_text=None, scoped=False):
    errors, warnings = [], []
    if (not isinstance(data, dict) or type(data.get('schema_version')) is not int
            or data['schema_version'] != 1 or not isinstance(data.get('assets'), list)):
        return ['须提供schema_version: 1及assets数组'], [], {}
    views, reused = {}, []
    for asset in data['assets']:
        if not isinstance(asset, dict):
            errors.append('asset须为对象'); continue
        plan = asset.get('view_plan', [])
        if not isinstance(plan, list):
            errors.append('view_plan须为数组'); continue
        for view in plan:
            if not isinstance(view, dict):
                errors.append('view_plan条目须为对象'); continue
            image_id = view.get('image_id')
            if not isinstance(image_id, str) or not IMAGE.fullmatch(image_id):
                errors.append(f'非法场景图号：{image_id!r}'); continue
            if not isinstance(view.get('name'), str) or not view['name'].strip():
                errors.append(f'{image_id}缺少视图名')
            separate = view.get('generate_separate_image', True)
            if not isinstance(separate, bool):
                errors.append(f'{image_id}独立生成标记须为布尔值'); continue
            if not separate:
                reused.append((asset.get('handle'), view)); continue
            if image_id in views:
                errors.append(f'重复独立图号：{image_id}'); continue
            views[image_id] = (asset.get('handle'), view)
    for handle, view in reused:
        target = views.get(view['image_id'])
        if target is None or target[0] != handle:
            errors.append(f"复用图号无同资产独立源：{view['image_id']}")
    graph = {}
    for image_id, (_, view) in views.items():
        source = view.get('source_image_id')
        if source is not None and (not isinstance(source, str) or source not in views):
            errors.append(f'{image_id}源图不存在：{source!r}'); continue
        if view.get('generation_method') == 'image_to_image' and source is None:
            errors.append(f'{image_id}图生图缺少直接源图')
        graph[image_id] = source
    # Iterative coloring avoids recursion limits on large projects.
    done = set()
    for node in graph:
        path, current = set(), node
        while current is not None and current in graph and current not in done:
            if current in path:
                errors.append(f'源图链成环（含自指）：{current}'); break
            path.add(current); current = graph[current]
        done.update(path)
    delivery = data.get('video_delivery', {})
    if not isinstance(delivery, dict):
        return errors + ['video_delivery须为对象'], warnings, {}
    records = delivery.get('clips', [])
    if not isinstance(records, list):
        return errors + ['video_delivery.clips须为数组'], warnings, {}
    clips, refs = {}, {}
    for entry in records:
        if not isinstance(entry, dict) or not isinstance(entry.get('id'), str):
            errors.append('Clip条目须有字符串id'); continue
        clip_id = entry['id']
        if not re.fullmatch(r'[1-9]\d*-[1-9]\d*', clip_id):
            errors.append(f'非法Clip编号：{clip_id}'); continue
        if clip_id in clips:
            errors.append(f'重复Clip：{clip_id}'); continue
        try:
            duration = number(entry.get('duration_seconds'), f'{clip_id}时长')
            if not 0 < duration <= 30:
                raise ValueError(f'{clip_id}时长须>0且≤30秒')
        except ValueError as exc:
            errors.append(str(exc)); duration = None
        clips[clip_id] = duration
        references = entry.get('scene_image_references', [])
        if not isinstance(references, list):
            errors.append(f'{clip_id}场景引用须为数组'); continue
        for ref in references:
            if not isinstance(ref, dict) or not isinstance(ref.get('image_id'), str):
                errors.append(f'{clip_id}场景引用缺少image_id'); continue
            image_id = ref['image_id']
            if image_id not in views:
                errors.append(f'{clip_id}引用不存在或弃用图：{image_id}'); continue
            try:
                interval = time_range(ref.get('time_range_seconds'), duration, f'{clip_id}/{image_id}')
            except ValueError as exc:
                errors.append(str(exc)); continue
            if 'actual_file' in ref and ref['actual_file'] != views[image_id][1].get('actual_file'):
                errors.append(f'{clip_id}/{image_id}文件版本与视图不一致')
            refs.setdefault(image_id, []).append((clip_id, interval))
    usage_errors, usage_warnings, usage_counts = validate_object_usage(data, clips)
    errors.extend(usage_errors)
    warnings.extend(usage_warnings)
    if views and not records:
        warnings.append('未提供Clip数据，双向映射待核验')
    for image_id, (_, view) in views.items():
        actual = refs.get(image_id, [])
        if 'clip_scope' not in view:
            if actual:
                warnings.append(f'{image_id}缺少反向clip_scope，双向映射待核验')
            continue
        try:
            declared = []
            for clip_id, interval in parse_scope(view['clip_scope']):
                if clip_id not in clips:
                    raise ValueError(f'{image_id}反向引用不存在的Clip：{clip_id}')
                declared.append((clip_id, time_range(interval, clips[clip_id], f'{image_id}/{clip_id}')))
            if Counter(declared) != Counter(actual):
                errors.append(f'{image_id}场景→Clip与Clip→场景双向映射不一致')
        except ValueError as exc:
            errors.append(str(exc))
    edit_order = delivery.get('edit_order')
    if edit_order is not None and (not isinstance(edit_order, list)
            or any(not isinstance(v, str) for v in edit_order)
            or len(edit_order) != len(set(edit_order)) or set(edit_order) != set(clips)):
        errors.append('edit_order须无重复且完整覆盖已登记Clip')
    if video_text is not None:
        parsed = contract.parse_clips(video_text)
        ids = [c.name for c in parsed]
        if not contract.outside_clip_starts(video_text):
            errors.append('视频文件须有Clip批-序标题')
        elif not set(ids) <= set(clips) or (not scoped and set(ids) != set(clips)):
            errors.append('视频标题Clip集合与总表范围不一致')
        if edit_order is not None and isinstance(edit_order, list):
            if ids != [v for v in edit_order if v in ids]:
                errors.append('视频文件顺序与edit_order不一致')
        for clip in parsed:
            if clip.name not in clips:
                continue
            declarations = {Decimal(v) for v in contract.DURATION.findall(clip.metadata)}
            if declarations != {clips[clip.name]}:
                errors.append(f'{clip.name}标题时长与总表不一致或缺失')
            for error in contract.check_clip(clip, clips[clip.name])[0]:
                errors.append(f'{clip.name}：{error}')
            try:
                titled = [(image_id, time_range(interval, clips[clip.name], clip.name))
                          for image_id, interval in image_title_refs(clip.metadata)]
                actual = [(image_id, interval) for image_id, usages in refs.items()
                          for cid, interval in usages if cid == clip.name]
                if Counter(titled) != Counter(actual):
                    errors.append(f'{clip.name}标题场景图/时段与总表不一致')
                # Registered S aliases in the copy body must belong to this Clip.
                for image_id in re.findall(r'@(S\d+(?:-\d+)?)(?![\w-])', clip.body):
                    if image_id not in {v[0] for v in actual}:
                        errors.append(f'{clip.name}正文引用未登记或弃用图：{image_id}')
            except ValueError as exc:
                errors.append(str(exc))
    if scene_text is not None:
        titles = {}
        for line in outside_lines(scene_text):
            match = SCENE_TITLE.match(line)
            if match:
                image_id = match.group(1)
                if image_id in titles:
                    errors.append(f'场景文件重复图号：{image_id}')
                titles[image_id] = line
        if not titles or not set(titles) <= set(views) or (not scoped and set(titles) != set(views)):
            errors.append('场景文件图号集合与总表范围不一致（含弃用或遗漏图）')
        for image_id, title in titles.items():
            if image_id not in views:
                continue
            source = views[image_id][1].get('source_image_id')
            declared = re.findall(r'源图(?:号)?\s*[:：]\s*(S\d+(?:-\d+)?)', title)
            if declared != ([source] if source else []):
                errors.append(f'{image_id}标题直接源图与总表不一致')
            clip_part = re.search(r'\bClip\s+(.+)$', title, re.I)
            try:
                titled = [] if clip_part is None else [
                    (cid, time_range(interval, clips.get(cid), f'{image_id}/{cid}'))
                    for cid, interval in parse_scope(clip_part.group(1))]
                if Counter(titled) != Counter(refs.get(image_id, [])):
                    errors.append(f'{image_id}场景标题适用Clip/时段与总表不一致')
            except ValueError as exc:
                errors.append(str(exc))
    if video_text is None:
        warnings.append('未提供视频文件，标题/正文与总表一致性未检查')
    if scene_text is None:
        warnings.append('未提供场景文件，标题/源图与总表一致性未检查')
    return errors, warnings, {'images': len(views), 'clips': len(clips),
                              'document_coverage': 'scoped' if scoped else 'complete',
                              **usage_counts}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--asset-registry', type=Path, required=True)
    parser.add_argument('--video', type=Path)
    parser.add_argument('--scenes', type=Path)
    parser.add_argument('--scoped', action='store_true')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    try:
        assets.load_asset_registry(args.asset_registry)
        data = json.loads(args.asset_registry.read_text(encoding='utf-8-sig'))
        errors, warnings, counts = validate_data(
            data, args.video.read_text(encoding='utf-8-sig') if args.video else None,
            args.scenes.read_text(encoding='utf-8-sig') if args.scenes else None, args.scoped)
        if args.report:
            args.report.write_text(json.dumps({'errors': errors, 'warnings': warnings,
                                              'counts': counts, 'scope': '数据/文本；非视觉/绑定验收'},
                                             ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    except (OSError, UnicodeError, ValueError, TypeError, InvalidOperation) as exc:
        print(f'INPUT ERROR: {exc}', file=sys.stderr); return 2
    for warning in warnings:
        print('WARN: ' + warning)
    for error in errors:
        print('FAIL: ' + error)
    print(('FAIL' if errors else 'PASS') + f'：项目数据检查 {counts}；未验证实图/平台绑定。')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
