#!/usr/bin/env python3
"""Check video-script-studio's four-section TEXT contract (stdlib only).

Input: one raw prompt, one fenced prompt with metadata outside, or multiple
'# Clip 1-1｜name' sections, each containing exactly one fenced prompt.
Optional --duration checks a single Clip; multi-Clip duration is read only from
outside-fence metadata such as '时长：8秒'. --dialogue-source must be a same-scope
truth document with dialogue in 「」 (not the whole project's unrelated lines).

This is a lexical/structural check, NOT semantic, model capability, real binding,
visual, speech-timing or speaker attribution validation. JSON/HTML and short-form
image/audio tasks are out of scope. Exit: 0 pass, 1 contract failure, 2 input error.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path
import re
import sys

HEADERS = ('参考素材职责', '一句话概述', '具体情节', '全局补充')
HEADER = re.compile(r'^\s*【([^】\n]+)】\s*$', re.M)
CLIP = re.compile(r'^#{1,6}\s+Clip\s+([1-9]\d*-[1-9]\d*)(?=\s|[｜|]|$)', re.I)
NUMBER = r'(?:\d+(?:\.\d+)?)'
TIME = re.compile(
    rf'^\s*({NUMBER})\s*(?:s|秒)?\s*[-–—~～至]\s*'
    rf'({NUMBER})\s*(?:s|秒)\s*[:：]\s*', re.M | re.I)
DURATION = re.compile(
    rf'(?:时长|duration)\s*[:：]\s*({NUMBER})\s*(?:秒|s)(?![A-Za-z])', re.I)
DIALOGUE = re.compile(r'「([^「」]*)」')
NO_DIALOGUE = '本段无对白（设计）'
FENCE = re.compile(r'^\s*(`{3,}|~{3,})([^\n]*)$')
MAX_CLIP_DURATION = Decimal(30)


@dataclass
class ClipText:
    name: str
    body: str
    metadata: str


def outside_clip_starts(text: str) -> list[tuple[int, str]]:
    starts = []
    fence = None
    offset = 0
    for line in text.splitlines(keepends=True):
        match = FENCE.match(line.rstrip('\r\n'))
        if match:
            marker, info = match.groups()
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not info.strip():
                fence = None
        elif fence is None:
            match = CLIP.match(line)
            if match:
                starts.append((offset, match.group(1)))
            elif re.match(r'^#{1,6}\s+Clip\b', line, re.I):
                raise ValueError('Clip 标题须使用正整数批-序，如 # Clip 1-1｜片段名')
        offset += len(line)
    if fence is not None:
        raise ValueError('代码围栏未闭合')
    return starts


def unwrap(name: str, text: str) -> ClipText:
    blocks, metadata, lines = [], [], []
    fence = None
    for line in text.splitlines(keepends=True):
        match = FENCE.match(line.rstrip('\r\n'))
        if match and fence is None:
            marker, info = match.groups()
            if info.strip().lower() not in ('', 'text', 'plaintext', 'txt'):
                raise ValueError(f'{name}: 只支持 text/plaintext/txt 或无语言的文本围栏')
            fence = marker
            lines = []
        elif match and fence and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence) and not match.group(2).strip():
            blocks.append(''.join(lines))
            fence = None
        elif fence:
            lines.append(line)
        else:
            metadata.append(line)
    if fence:
        raise ValueError(f'{name}: 代码围栏未闭合')
    if len(blocks) > 1:
        raise ValueError(f'{name}: 每个 Clip 只接收一个提示词复制块，请分开检查其他交付物')
    return ClipText(name, blocks[0] if blocks else text, ''.join(metadata) if blocks else '')


def parse_clips(text: str) -> list[ClipText]:
    starts = outside_clip_starts(text)
    if not starts:
        return [unwrap('单片段', text)]
    if len({name for _, name in starts}) != len(starts):
        raise ValueError('Clip 编号重复')
    # A leading preamble must not hide an unlabelled prompt.
    if re.search(r'【(?:参考素材职责|具体情节)】', text[:starts[0][0]]):
        raise ValueError('首个 Clip 标题前含未编号提示词，请单独检查')
    clips = []
    for index, (start, name) in enumerate(starts):
        end = starts[index + 1][0] if index + 1 < len(starts) else len(text)
        clips.append(unwrap(name, text[start:end]))
    return clips


def quote_errors(text: str) -> list[str]:
    inside = False
    for char in text:
        if char == '「':
            if inside:
                return ['台词引号嵌套或未闭合']
            inside = True
        elif char == '」':
            if not inside:
                return ['台词引号不配对']
            inside = False
    if inside:
        return ['台词引号未闭合']
    if any(not value.strip() for value in DIALOGUE.findall(text)):
        return ['存在空台词']
    return []


def check_clip(clip: ClipText, duration: Decimal | None = None) -> tuple[list[str], list[str]]:
    errors = quote_errors(clip.body)
    if duration is not None and duration > MAX_CLIP_DURATION:
        errors.append(f'声明时长 {duration}s 超过单个 Clip 硬上限30秒；须压缩或顺延到下一个 Clip')
    matches = list(HEADER.finditer(clip.body))
    if tuple(m.group(1) for m in matches) != HEADERS:
        errors.append('四标题须各出现一次且顺序为：' + ' → '.join(HEADERS))
        return errors, []
    parts = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(clip.body)
        part = clip.body[match.end():end].strip()
        parts[match.group(1)] = part
        if not part:
            errors.append(f'【{match.group(1)}】内容为空')
    scene = parts['具体情节']
    beats = list(TIME.finditer(scene))
    if not beats:
        errors.append('具体情节缺少秒级时间轴，如 0s-3s：')
    else:
        previous = Decimal(0)
        if scene[:beats[0].start()].strip():
            errors.append('具体情节首个时间段前有未分配内容')
        for index, beat in enumerate(beats):
            start, end = map(Decimal, beat.groups())
            label = f'{start}s-{end}s'
            if start != previous:
                errors.append(f'{label}：时间轴有缺口/重叠或未从0开始（应接 {previous}s）')
            if end <= start:
                errors.append(f'{label}：结束时间必须大于开始时间')
            if start > MAX_CLIP_DURATION or end > MAX_CLIP_DURATION:
                errors.append(f'{label}：时间轴超过单个 Clip 硬上限30秒；须压缩或顺延到下一个 Clip')
            next_start = beats[index + 1].start() if index + 1 < len(beats) else len(scene)
            content = scene[beat.end():next_start].strip()
            if not content:
                errors.append(f'{label}：演出内容为空')
            # Catch range-like lines that did not satisfy TIME, rather than
            # silently treating malformed timestamps as prose in the prior beat.
            if re.search(r'^\s*\d[^\n]*[-–—~～至][^\n]*[:：]', content, re.M):
                errors.append(f'{label}：含无法解析的时间段，请统一秒级格式')
            previous = end
        if duration is not None and previous != duration:
            errors.append(f'时间轴终点 {previous}s 与声明时长 {duration}s 不符')
    dialogue = DIALOGUE.findall(scene)
    if DIALOGUE.findall(clip.body) != dialogue:
        errors.append('台词必须全部内联在【具体情节】的对应时间段')
    if not dialogue and NO_DIALOGUE not in clip.body:
        errors.append(f'无对白片段须显式标注“{NO_DIALOGUE}”')
    if dialogue and NO_DIALOGUE in clip.body:
        errors.append('既有台词又声明本段无对白')
    if re.search(r'\{[^{}\n]+\}|<[^<>\n]+>|[（(](?:背景音乐|背景播放|配乐|音乐)[^）)\n]*[）)]', clip.body):
        errors.append('残留旧式台词/声音标签：对白用「」，音效/音乐用内联自然句')
    if re.search(r'^\s*(?:声音|音效|音乐|台词)\s*[:：]', scene, re.M):
        errors.append('声音/台词不得独立成栏，应内联到动作中')
    if re.search(r'^\s*(?:模型|画幅|时长|分辨率|速度|model|duration|resolution)\s*[:：]', clip.body, re.M | re.I):
        errors.append('平台设置应写在复制块外')
    if re.search(r'^\s*(?:[A-Za-z\u4e00-\u9fff]+\s*)?(?:固定声线|音色描述|Voice Description|Vocal profile)\s*[:：]', clip.body, re.M | re.I):
        errors.append('视频正文不附固定声线或音色描述；保留对应动作中的当下语气与发声')
    if '无字幕' not in parts['全局补充'] or '无水印' not in parts['全局补充']:
        errors.append('全局补充须声明无字幕、无水印')
    return errors, dialogue


def check_document(text: str, duration: Decimal | None = None,
                   dialogue_source: str | None = None) -> tuple[list[str], int]:
    clips = parse_clips(text)
    if duration is not None and len(clips) != 1:
        raise ValueError('--duration 仅用于单 Clip；多 Clip 在各自复制块外声明时长')
    failures, actual = [], []
    for clip in clips:
        declared = {Decimal(value) for value in DURATION.findall(clip.metadata)}
        if len(declared) > 1:
            raise ValueError(f'{clip.name}: 块外时长声明冲突')
        expected = next(iter(declared), None)
        if duration is not None:
            if expected is not None and duration != expected:
                raise ValueError(f'{clip.name}: --duration 与块外时长声明冲突')
            expected = duration
        if expected is not None and (not expected.is_finite() or expected <= 0):
            raise ValueError('时长必须是有限正数')
        errors, lines = check_clip(clip, expected)
        failures.extend(f'{clip.name}: {error}' for error in errors)
        actual.extend(lines)
    if dialogue_source is not None:
        source_errors = quote_errors(dialogue_source)
        if source_errors:
            raise ValueError('对白真值稿：' + '；'.join(source_errors))
        expected_lines = DIALOGUE.findall(dialogue_source)
        if not expected_lines and NO_DIALOGUE not in dialogue_source:
            raise ValueError('真值稿无「台词」，须提供同范围台词或显式无对白标记')
        wanted, got = Counter(expected_lines), Counter(actual)
        for value, count in (wanted - got).items():
            failures.append(f'对白缺失 {count} 次：「{value}」')
        for value, count in (got - wanted).items():
            failures.append(f'对白新增/重复 {count} 次：「{value}」')
    return failures, len(clips)


def positive_duration(value: str) -> Decimal:
    try:
        parsed = Decimal(value)
    except InvalidOperation:
        raise argparse.ArgumentTypeError('时长须为数字') from None
    if not parsed.is_finite() or parsed <= 0:
        raise argparse.ArgumentTypeError('时长必须是有限正数')
    return parsed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--file', required=True, type=Path)
    parser.add_argument('--duration', type=positive_duration, help='单 Clip 预期时长（秒，硬上限30秒）')
    parser.add_argument('--dialogue-source', type=Path, help='同范围对白真值稿，台词用「」')
    args = parser.parse_args()
    try:
        if args.duration is not None and (not args.duration.is_finite() or args.duration <= 0):
            raise ValueError('时长必须是有限正数')
        source = args.dialogue_source.read_text(encoding='utf-8-sig') if args.dialogue_source else None
        failures, count = check_document(args.file.read_text(encoding='utf-8-sig'), args.duration, source)
    except (OSError, UnicodeError, ValueError, InvalidOperation) as exc:
        print(f'INPUT ERROR: {exc}', file=sys.stderr)
        return 2
    for error in failures:
        print(f'FAIL: {error}')
    print(f'{"FAIL" if failures else "PASS"}: {count} Clip；仅文本契约检查，语义/绑定/生成结果未验收。')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
