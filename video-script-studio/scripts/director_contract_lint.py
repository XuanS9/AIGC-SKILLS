#!/usr/bin/env python3
"""Check video-script-studio's video prompt TEXT contract (stdlib only).

Format: the Higgsfield / Dreamina Seedance 2.5 block structure written in
Chinese (block labels, fields and prose); dialogue lines stay in English. Dialogue follows Higgsfield: every line lives in
[声音] as '起s-止s｜说话人＋状态＋说：{English line}', never in the action
segments. A clip with people opens on a ~1 s positioning shot whose
'0s-1s｜<名字>轻声：{Hm.}' line fixes the blocking (Hell Grind 'hm' trick).
See references/template-general-director-2-5.md § 1 块结构.

Input: one raw prompt, one fenced prompt with metadata outside, or multiple
'# Clip 1-1｜name' sections, each containing exactly one fenced prompt.
Optional --duration checks a single Clip; multi-Clip duration is read only from
outside-fence metadata such as '时长：8秒'. --dialogue-source is a same-scope
truth document with dialogue in {} or 「」.

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

# Block order (Higgsfield omni-reference template, written in Chinese).
BLOCK_ORDER = ('角色', '道具', '场景', '动作与声音参考', '生成目标',
               '具体情节', '视觉风格', '镜头', '声音', '保持一致')
REQUIRED_BLOCKS = ('生成目标', '具体情节', '视觉风格', '镜头', '声音', '保持一致')
REFERENCE_BLOCKS = ('角色', '道具', '场景', '动作与声音参考')
ENGLISH_LABELS = re.compile(r'^\s*\[(Characters|Props|Scenes|Motion and Audio|Generation Goal|Stage\b[^\]]*|'
                            r'Visual Style|Camera|Audio|Maintain Consistency)\]\s*$', re.M)
HEADERS = REQUIRED_BLOCKS  # kept for importers; the required blocks
BLOCK = re.compile(r'^\s*\[([^\]\n]+)\]\s*$', re.M)
HEADER = BLOCK
LEGACY_HEADER = re.compile(r'^\s*[【\[](参考素材职责|一句话概述|全局补充)[】\]]\s*$|^\s*【具体情节】\s*$|^\s*\[阶段\s*\d', re.M)
CLIP = re.compile(r'^#{1,6}\s+Clip\s+([1-9]\d*-[1-9]\d*)(?=\s|[｜|]|$)', re.I)
NUMBER = r'(?:\d+(?:\.\d+)?)'
# Segment head inside [具体情节]:  1s-4s｜切至双人中景｜视场角47°｜固定
SEGMENT = re.compile(
    rf'^\s*({NUMBER})\s*s\s*-\s*({NUMBER})\s*s\s*[｜|]\s*([^｜|\n]+?)\s*[｜|]'
    r'\s*视场角\s*(\d+)\s*°\s*[｜|]\s*([^｜|\n]+?)\s*$', re.M)
TIME_LOOSE = re.compile(rf'^\s*{NUMBER}\s*s?\s*[-–—~～至]\s*{NUMBER}\s*(?:s|秒)', re.M)
TIME = re.compile(rf'^\s*({NUMBER})\s*s\s*-\s*({NUMBER})\s*s\s*[｜|]', re.M)
# '对白' is parsed only to report it: dialogue belongs in [声音].
SEGMENT_FIELDS = ('画面', '运镜', '动作', '表情', '听者', '声音', '对白')
REQUIRED_FIELDS = ('画面', '运镜', '动作', '表情')
FOV_ANCHORS = {180, 107, 84, 63, 47, 29, 18, 12, 8}
# Longest first so 中近景 is not read as 中景 or 近景.
SIZE_RANK = [('大特写', 7), ('大远景', 0), ('大全景', 1), ('中全景', 2), ('中近景', 4), ('过肩', 4),
             ('特写', 6), ('插入', 6), ('远景', 0), ('全景', 1), ('中景', 3), ('近景', 5)]
DURATION = re.compile(
    rf'(?:时长|duration)\s*[:：]\s*({NUMBER})\s*(?:秒|s)(?![A-Za-z])', re.I)
# Higgsfield/Dreamina bracket syntax: {dialogue}, <sound effect>, (music).
DIALOGUE = re.compile(r'\{([^{}\n]*)\}')
LEGACY_DIALOGUE = re.compile(r'「[^「」]*」')
SFX = re.compile(r'<([^<>\n]+)>')
MUSIC = re.compile(r'[（(]([^）)\n]*)[）)]')
NO_DIALOGUE = '本段无对白（设计）'
# Dialogue line inside [声音]:  6s-9s｜母亲放柔声音说：{You can let go now.}
AUDIO_LINE = re.compile(
    rf'^\s*({NUMBER})\s*s\s*-\s*({NUMBER})\s*s\s*[｜|]\s*([^：:\n{{}}]+?)\s*[:：]\s*\{{([^{{}}\n]*)\}}\s*[。.]?\s*$', re.M)
# The positioning-second vocalisation (Hell Grind "hm"), written {Hm.}.
HM = re.compile(r'^\s*h+m+[.。!！]?\s*$', re.I)
PEOPLE = re.compile(r'^\s*恰好\s*(\d+)\s*人', re.M)
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
    if blocks:
        return ClipText(name, blocks[0], ''.join(metadata))
    # Unfenced studio text still has block-external title/settings metadata.
    first = next((m for m in BLOCK.finditer(text) if block_name(m.group(1)) in BLOCK_ORDER), None)
    if first is None:
        return ClipText(name, text, '')
    head = text[:first.start()]
    # Only title/settings metadata may sit above an unfenced prompt.
    stray = [l for l in head.splitlines() if l.strip() and not re.match(
        r'^\s*(#|时长|画幅|分辨率|模型|模式|平台|Model|Duration|Resolution|Aspect|Mode|Platform)', l, re.I)]
    if stray:
        return ClipText(name, text, '')
    return ClipText(name, text[first.start():], head)


def parse_clips(text: str) -> list[ClipText]:
    starts = outside_clip_starts(text)
    if not starts:
        return [unwrap('单片段', text)]
    if len({name for _, name in starts}) != len(starts):
        raise ValueError('Clip 编号重复')
    # A leading preamble must not hide an unlabelled prompt.
    if re.search(r'(?m)^\s*\[(?:角色|生成目标|阶段)', text[:starts[0][0]]):
        raise ValueError('首个 Clip 标题前含未编号提示词，请单独检查')
    clips = []
    for index, (start, name) in enumerate(starts):
        end = starts[index + 1][0] if index + 1 < len(starts) else len(text)
        clips.append(unwrap(name, text[start:end]))
    return clips


def quote_errors(text: str) -> list[str]:
    inside = False
    for char in text:
        if char == '{':
            if inside:
                return ['台词括号嵌套或未闭合']
            inside = True
        elif char == '}':
            if not inside:
                return ['台词括号不配对']
            inside = False
    if inside:
        return ['台词括号未闭合']
    if any(not value.strip() for value in DIALOGUE.findall(text)):
        return ['存在空台词']
    return []


def block_name(label: str) -> str:
    return label.strip()


def split_blocks(body: str) -> list[tuple[str, str, str]]:
    """[(block name, raw label, content)] in order."""
    marks = list(BLOCK.finditer(body))
    out = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(body)
        out.append((block_name(m.group(1)), m.group(1), body[m.end():end].strip()))
    return out


def size_rank(size: str) -> int | None:
    low = size.lower()
    for word, rank in SIZE_RANK:
        if word in low:
            return rank
    return None


def check_clip(clip: ClipText, duration: Decimal | None = None) -> tuple[list[str], list[str]]:
    errors = quote_errors(clip.body)
    if duration is not None and duration > MAX_CLIP_DURATION:
        errors.append(f'声明时长 {duration}s 超过单个 Clip 硬上限30秒；须压缩或顺延到下一个 Clip')
    if LEGACY_HEADER.search(clip.body):
        errors.append('旧标题已停用：用 [角色] [道具] [场景] [动作与声音参考] [生成目标] [具体情节] [视觉风格] [镜头] [声音] [保持一致]；【】是 Dreamina 字幕括号')
        return errors, []
    if ENGLISH_LABELS.search(clip.body):
        errors.append('块标签用中文：[角色] [道具] [场景] [动作与声音参考] [生成目标] [具体情节] [视觉风格] [镜头] [声音] [保持一致]')
        return errors, []
    if LEGACY_DIALOGUE.search(clip.body):
        errors.append('台词写成 对白：说话人＋状态＋说：{English line}，不用「」')
    blocks = split_blocks(clip.body)
    if clip.body[:clip.body.find('[')].strip() if '[' in clip.body else clip.body.strip():
        errors.append('首个块之前有未归属内容')
    names = [b[0] for b in blocks]
    unknown = [raw for name, raw, _ in blocks if name not in BLOCK_ORDER]
    if unknown:
        errors.append('未知块：' + '、'.join(f'[{u}]' for u in unknown) + '；可用块：' + ' → '.join(BLOCK_ORDER))
    for req in REQUIRED_BLOCKS:
        if req not in names:
            errors.append(f'缺少 [{req}] 块')
    order = [BLOCK_ORDER.index(n) for n in names if n in BLOCK_ORDER]
    if order != sorted(order):
        errors.append('块顺序须为：' + ' → '.join(BLOCK_ORDER))
    for name in set(names):
        if names.count(name) > 1:
            errors.append(f'[{name}] 重复出现')
    for name, raw, content in blocks:
        if not content:
            errors.append(f'[{raw}] 内容为空')
    if errors:
        return errors, []
    parts = {name: content for name, _, content in blocks}
    segments = split_segments(parts['具体情节'])
    errors.extend(segment_errors(parts['具体情节'], segments, duration))
    audio = parts['声音']
    lines = audio_lines(audio)
    if DIALOGUE.findall(clip.body) != [line['text'] for line in lines]:
        errors.append('台词 {…} 只写在 [声音] 的对白行 “起s-止s｜说话人＋状态＋说：{English line}”'
                      '（Higgsfield：动作描述里的台词会被演成行为）')
    end = segments[-1]['end'] if segments else Decimal(0)
    for line in lines:
        if not (0 <= line['start'] < line['end'] <= end):
            errors.append(f"对白行 {line['start']}s-{line['end']}s 超出 [具体情节] 时间轴 0s-{end}s")
    positioning = [line for line in lines if HM.match(line['text']) and line['start'] == 0]
    dialogue = [line['text'] for line in lines if line not in positioning]
    people = PEOPLE.search(parts.get('角色', ''))
    if people and int(people.group(1)) >= 1 and segments:
        if not positioning:
            errors.append('有人物的 Clip 第一秒是定位秒，须在 [声音] 写一声 hm：'
                          f"“0s-{segments[0]['end']}s｜<名字>轻声：{{Hm.}}”，用来锁定人物站位")
        elif positioning[0]['end'] != segments[0]['end']:
            errors.append(f"定位 hm 的时间段须与第一段 0s-{segments[0]['end']}s 一致")
    if people and int(people.group(1)) == 0 and positioning:
        errors.append('恰好 0 人的 Clip 没有人能发出定位 hm，删掉这一行')
    sfx_ok = [x for seg in segments for line in seg['fields'].get('声音', []) for x in SFX.findall(line)]
    if SFX.findall(clip.body) != sfx_ok:
        errors.append('音效 <…> 只写在 [具体情节] 各段的 “声音：” 行')
    if not dialogue and NO_DIALOGUE not in audio:
        errors.append(f'无对白片段须在 [声音] 写“{NO_DIALOGUE}”')
    if dialogue and NO_DIALOGUE in audio:
        errors.append('既有台词又声明无对白')
    if dialogue and not re.search(r'对白语言\s*[:：]', audio):
        errors.append('有台词时 [声音] 须写 “对白语言：英语。”')
    if any(re.search(r'[\u4e00-\u9fff]', line) for line in dialogue):
        errors.append('台词原句用英文：{…} 内不写中文')
    music = [m for m in MUSIC.findall(clip.body) if re.search(r'music|score|song|melody|BGM|音乐|配乐|旋律|乐', m, re.I)]
    if any(re.search(r'\bno\b|无|不要|没有|silence', m, re.I) for m in music):
        errors.append('静音不写进 () 音乐括号：() 是音乐通道；在 [声音] 末尾写 NO BGM')
    if 'NO BGM' not in audio and not music:
        errors.append('[声音] 须写 NO BGM（或用 () 写用户要求的音乐）')
    consistency = parts['保持一致']
    if '无字幕' not in consistency or '无水印' not in consistency:
        errors.append('[保持一致] 须写 “无字幕、无水印。”')
    if re.search(r'^\s*(?:模型|画幅|时长|分辨率|model|duration|resolution|aspect ratio)\s*[:：]', clip.body, re.M | re.I):
        errors.append('平台设置应写在复制块外')
    voice = re.compile(r'(?:固定声线|音色描述|音色|Voice Description|Vocal profile|Voice)\s*[:：]', re.I)
    for name in ('生成目标', '具体情节', '视觉风格', '镜头', '保持一致'):
        if voice.search(parts[name]):
            errors.append(f'音色描述只写在 [角色]，不放 [{name}]')
    errors.extend(readability_errors(clip.body, parts, segments))
    return errors, dialogue


def audio_lines(audio: str) -> list[dict]:
    """Timed dialogue lines in [声音]: [{start, end, speaker, text}]."""
    return [dict(start=Decimal(m.group(1)), end=Decimal(m.group(2)), speaker=m.group(3).strip(), text=m.group(4))
            for m in AUDIO_LINE.finditer(audio)]


def split_segments(scene: str) -> list[dict]:
    """[{start, end, size, fov, move, head, fields{name: [lines]}, end_state, raw}]"""
    heads = list(TIME.finditer(scene))
    out = []
    for i, m in enumerate(heads):
        line_end = scene.find('\n', m.end())
        line_end = len(scene) if line_end < 0 else line_end
        head = scene[m.start():line_end].strip()
        start_of_line = scene.rfind('\n', 0, m.end()) + 1
        head = scene[start_of_line:line_end].strip()
        body_end = heads[i + 1].start() if i + 1 < len(heads) else len(scene)
        body = scene[line_end:body_end].strip()
        full = SEGMENT.match(head)
        fields, end_state = {}, None
        for line in body.splitlines():
            line = line.strip()
            if not line:
                continue
            f = re.match(r'^(画面|运镜|动作|表情|听者|声音|对白)\s*[:：]\s*(.*)$', line)
            e = re.match(r'^→\s*结束\s*[:：]\s*(.*)$', line)
            if f:
                fields.setdefault(f.group(1), []).append(f.group(2))
            elif e:
                end_state = e.group(1)
            else:
                fields.setdefault('_stray', []).append(line)
        out.append(dict(start=Decimal(m.group(1)), end=Decimal(m.group(2)),
                        size=full.group(3) if full else '', fov=int(full.group(4)) if full else None,
                        move=full.group(5) if full else '', head=head, full=bool(full),
                        fields=fields, end_state=end_state, raw=body))
    return out


def segment_errors(scene: str, segments: list, duration) -> list[str]:
    errors = []
    if not segments:
        errors.append('[具体情节] 缺少时间段，如 “0s-1s｜双人全景｜视场角84°｜固定”')
        return errors
    if scene[:TIME.search(scene).start()].strip():
        errors.append('[具体情节] 首个时间段前有未分配内容')
    if TIME_LOOSE.search(scene) and len(TIME_LOOSE.findall(scene)) != len(segments):
        errors.append('[具体情节] 含无法解析的时间段：段头须为 “1s-4s｜景别｜视场角47°｜运镜”')
    previous = Decimal(0)
    for seg in segments:
        label = f"{seg['start']}s-{seg['end']}s"
        if not seg['full']:
            errors.append(f'{label}：段头须为 “{label}｜景别｜视场角N°｜运镜”')
            previous = seg['end']
            continue
        if seg['start'] != previous:
            errors.append(f'{label}：时间轴有缺口/重叠或未从0开始（应接 {previous}s）')
        if seg['end'] <= seg['start']:
            errors.append(f'{label}：结束时间必须大于开始时间')
        if seg['end'] > MAX_CLIP_DURATION:
            errors.append(f'{label}：时间轴超过单个 Clip 硬上限30秒；须压缩或顺延到下一个 Clip')
        if size_rank(seg['size']) is None:
            errors.append(f"{label}：景别 “{seg['size']}” 不是标准景别（远景/全景/中景/中近景/近景/特写…）")
        if seg['fov'] not in FOV_ANCHORS:
            errors.append(f"{label}：视场角{seg['fov']}° 不在锚点内（84/63/47/29/18/12°）")
        for name in REQUIRED_FIELDS:
            if name not in seg['fields']:
                errors.append(f'{label}：缺少 “{name}：” 行')
        if seg['end_state'] is None:
            errors.append(f'{label}：须以 “→ 结束：” 收尾')
        if '对白' in seg['fields']:
            errors.append(f'{label}：台词不写在段内；移到 [声音]：“{label}｜说话人＋状态＋说：{{English line}}”，'
                          '段内 动作/表情 只写看得见的说话动作（张口、气息、姿态）')
        if seg['fields'].get('_stray'):
            errors.append(f"{label}：有未归类的行 “{seg['fields']['_stray'][0][:16]}…”；只用 画面/运镜/动作/表情/听者/声音 与 → 结束")
        previous = seg['end']
    if duration is not None and previous != duration:
        errors.append(f'时间轴终点 {previous}s 与声明时长 {duration}s 不符')
    return errors


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
        # Truth documents (scripts) may keep 「」; normalise to the prompt's {} form.
        dialogue_source = re.sub(r'「([^「」]*)」', r'{\1}', dialogue_source)
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


# Higgsfield / Dreamina Seedance 2.5 model-readability rules
# (references/template-general-director-2-5.md § 模型可读性).
HANDLE = re.compile(r'@[^\s，。；、：:,;.（）()「」【】\[\]{}<>｜|]+')
META_TERMS = re.compile(
    r'镜头\s*\d+|落幅|起幅|机位|关系中景|关系全景|关系近景|省略[^，。；]{0,12}|'
    r'承接[^，。；]{0,8}|完成后才|确认[^，。；]{0,10}才|本镜|上一镜|下一镜|前一段|上一段|'
    r'同上|如前|承上|见上文|Clip\s*\d+-\d+|第\s*\d+\s*批|(?i:as above|previous shot|previous clip|same as before)')
CUT_LOCK = re.compile(r'只在指定处切镜，镜头不会自行切换')


def readability_errors(body: str, parts: dict, segments: list) -> list[str]:
    errors = []
    prose = '\n'.join([parts['生成目标'], parts['具体情节'], parts['视觉风格'], parts['镜头'],
                       parts['声音'], parts['保持一致']])
    found = HANDLE.findall(prose)
    if found:
        errors.append(f'正文出现素材调用名 {found[0]}：@ 只放在 [角色]/[道具]/[场景]/[动作与声音参考]，其余用中文名')
    hits = META_TERMS.findall(prose)
    if hits:
        kinds = list(dict.fromkeys(re.sub(r'\d+', 'N', re.sub(r'^(省略|承接|确认).*', r'\1…', h)) for h in hits))
        errors.append(f'正文含模型读不懂的编辑/元语言 {len(hits)} 处：' + '、'.join(kinds) + '；改写为画面上可见的动作与结束状态')
    has_cut = any(re.search(r'切至|硬切|反打|切回', seg['size']) for seg in segments)
    if has_cut and not CUT_LOCK.search(parts['镜头']):
        errors.append('有切镜时 [镜头] 须写 “只在指定处切镜，镜头不会自行切换。”')
    clause = re.compile(r'[。；，,.;]')
    # Plot = action, expression and listener lines; positions/light may be restated
    # in [保持一致] (Higgsfield's Maintain Consistency repeats spatial direction).
    stage_clauses = {c.strip() for seg in segments
                     for name in ('动作', '表情', '听者') for line in seg['fields'].get(name, [])
                     for c in clause.split(line) if len(c.strip()) >= 6}
    repeated = [c for c in clause.split(parts['保持一致'] + '\n' + parts['视觉风格'])
                if len(c.strip()) >= 6 and c.strip() in stage_clauses]
    if repeated:
        errors.append(f'[视觉风格]/[保持一致] 复述具体情节内容：“{repeated[0].strip()[:20]}…”')
    chars = parts.get('角色', '')
    count = re.search(r'^\s*恰好\s*(\d+)\s*人', chars, re.M)
    if chars and not count:
        errors.append('[角色] 首行须写人数：“恰好 N 人，不出现其他人：…”')
    people = int(count.group(1)) if count else 0
    if people >= 2 and len(re.findall(r'身高\s*\d{3}\s*cm', chars)) < people:
        errors.append(f'[角色] 写了 {people} 人，须给每个人写身高（cm），防止身高趋同；生物不算人数，可写体长')
    if '场景' in parts and '场景只含参考所示内容' not in parts['场景']:
        errors.append('[场景] 须写 “场景只含参考所示内容，不增加家具或房间。”')
    return errors


# Clip boundary isolation (narrative-planning.md § Clip 边界隔离). WARN only:
# literal checks have false positives; cuttability needs the rough cut.
MOVING_TAIL = re.compile(r'正在|推近|推进|拉远|后拉|跟随|跟拍|追随|环绕|横移|摇向|摇到|甩向|升起|俯冲|加速|冲向|奔跑|转身|走出|出画|离开画面|仍在说|未说完|余音|手持')
STILL_TAIL = re.compile(r'停住|静止|定格|站定|坐定|稳住|镜头停|不动|停在|固定')
ANGLE_CHANGE = re.compile(r'反打|过肩|换角度|另一侧|对面|俯拍|仰拍|侧面|背后|跳时|换场')
STATE_WORDS = re.compile(r'站|坐|蹲|跪|躺|位于|画面[左右中]|在[^，。]{0,8}(前|后|旁|边|左|右|中央|上)|面向|朝向|握|持|手')


def beat_texts(clip: ClipText) -> list[tuple[str, str, str]]:
    """[(shot size, camera move, segment text)] per segment."""
    scene = next((c for n, _, c in split_blocks(clip.body) if n == '具体情节'), '')
    return [(seg['size'], seg['move'], seg['raw']) for seg in split_segments(scene)]


def shot_size(size: str) -> str | None:
    return size if size_rank(size) is not None else None


# Camera move size and its minimum sensible duration (Higgsfield camera guide:
# "slow dolly push from medium shot to tight close-up over 8 seconds";
# micro-moves "10–15 cm over 7 seconds"). Starting heuristics, WARN only.
CAMERA_MOVES = [
    (re.compile(r'固定|定镜|锁定'), 0, '固定'),
    (re.compile(r'微推|微拉|轻推|轻拉'), Decimal(3), '微推/微拉'),
    (re.compile(r'环绕|绕拍|弧线'), Decimal(4), '环绕'),
    (re.compile(r'升降|升起|下降|摇臂|揭示'), Decimal(5), '升降/揭示'),
    (re.compile(r'横移|跟拍|跟随|平移|追拍'), Decimal(3), '横移/跟拍'),
    (re.compile(r'推近|推进|拉远|后拉|前推'), Decimal(3), '推拉'),
    (re.compile(r'手持'), 0, '手持'),
    (re.compile(r'摇镜|横摇|竖摇|甩镜'), Decimal(1), '摇镜'),
]
CAMERA_CONFLICTS = [('推近', '横摇'), ('环绕', '摇镜'), ('固定', '手持'), ('固定', '推近'), ('竖摇', '推近')]
CAMERA_MEASURE = re.compile(r'\d+(?:\.\d+)?\s*(?:秒|cm|厘米|米|m\b|km/h|°)')
EXPRESSION_CUES = re.compile(r'眼|瞳|睫|眉|嘴|唇|下颌|下巴|鼻|呼吸|喉|吞咽|脸颊|面颊|额|手指|指尖|拳|肩|眼眶|泪')
CLOSE = 5  # rank of 近景 and tighter
LAYOUT_WORDS = re.compile(r'前景|中景|背景|远处|近处|画面[左右上下中]|左侧|右侧|左下|右下|左上|右上|中央|上方|下方|身后|后方|前方')
ACTION_DETAIL = re.compile(r'\d+(?:\.\d+)?\s*(?:秒|cm|厘米|mm|米|km/h|°|次|下)|先|随后|然后|接着|再')


def camera_kind(move: str):
    for pattern, minimum, name in CAMERA_MOVES:
        if pattern.search(move):
            return name, minimum
    return None, 0


def size_jump(text: str) -> int:
    """Number of shot-size steps a push/pull spans, from '从A…到B' in the camera line."""
    m = re.search(r'从\s*([^\s，。到至]+?)\s*(?:推近|推进|拉远|后拉|拉|推)?\s*(?:到|至)\s*([^\s，。]+)', text)
    if not m:
        return 0
    a, b = size_rank(m.group(1)), size_rank(m.group(2))
    return abs(a - b) if a is not None and b is not None else 0


def craft_warnings(text: str) -> list[str]:
    """Camera, expression, listener and density checks per segment (WARN only)."""
    warnings = []
    for clip in parse_clips(text):
        blocks = {n: c for n, _, c in split_blocks(clip.body)}
        scene = blocks.get('具体情节', '')
        people = re.search(r'恰好\s*(\d+)\s*人', blocks.get('角色', ''))
        many = people is not None and int(people.group(1)) >= 2
        for seg in split_segments(scene):
            if not seg['full']:
                continue
            label = f"{clip.name} {seg['start']}s-{seg['end']}s"
            length = seg['end'] - seg['start']
            camera_line = ' '.join(seg['fields'].get('运镜', []))
            kind, minimum = camera_kind(seg['move'] + ' ' + camera_line)
            moving = kind not in (None, '固定')
            if moving and kind != '手持' and not CAMERA_MEASURE.search(camera_line):
                warnings.append(f'{label}: 运镜“{seg["move"]}”未写距离、秒数或速度；写成“用 N 秒从…到…”或“以 N km/h 横移”')
            jump = size_jump(camera_line)
            if kind == '推拉' and jump >= 2:
                minimum = max(minimum, Decimal(6))
            if moving and length < minimum:
                warnings.append(f'{label}: {kind}运镜只给了 {length} 秒，建议至少 {minimum} 秒（运镜幅度越大，时长越长）')
            for a, b in CAMERA_CONFLICTS:
                if a in camera_line + seg['move'] and b in camera_line + seg['move']:
                    warnings.append(f'{label}: 同一段同时有“{a}”和“{b}”；一镜一个主运动')
            rank = size_rank(seg['size'])
            expression = ' '.join(seg['fields'].get('表情', []))
            cues = len(set(EXPRESSION_CUES.findall(expression)))
            if rank is not None and rank >= CLOSE and cues < 2 and not expression.startswith('不适用'):
                warnings.append(f'{label}: {seg["size"]}的表情只有 {cues} 个可见线索；近景/特写写 2–4 个（眼、眉、嘴、呼吸、手）')
            if cues > 5:
                warnings.append(f'{label}: 表情线索 {cues} 个，偏多；一次情绪变化写 2–4 个即可')
            if many and rank is not None and rank <= 3 and '听者' not in seg['fields'] and not expression.startswith('不适用'):
                warnings.append(f'{label}: 两人以上同框却没写“听者：”；画面里其他人也要有可见反应')
            picture = ' '.join(seg['fields'].get('画面', []))
            if len(set(LAYOUT_WORDS.findall(picture))) < 2:
                warnings.append(f'{label}: 画面只有 {len(set(LAYOUT_WORDS.findall(picture)))} 个方位词；写清前景/中景/背景与画面左/右/上/下各有什么')
            action = ' '.join(seg['fields'].get('动作', []))
            if length >= 2 and not (ACTION_DETAIL.search(action) or len(re.findall(r'[，；]', action)) >= 2):
                warnings.append(f'{label}: 动作写得太简略；写起势→过程→结果，并给出幅度（cm）、用时（秒）或速度（km/h）')
            actions = len(re.findall(r'[，；。]', action))
            if moving and kind in ('环绕', '升降/揭示') and actions > 3:
                warnings.append(f'{label}: 大运镜段动作偏多；运镜幅度大时动作要少（每5秒1–2个主要动作）')
    return warnings


# Clip boundary isolation (narrative-planning.md § Clip 边界隔离). WARN only.
def boundary_warnings(text: str) -> list[str]:
    warnings = []
    rows = [(c, beat_texts(c)) for c in parse_clips(text)]
    for clip, beats in rows:
        if not beats:
            continue
        (fsize, fmove, first), (lsize, lmove, last) = beats[0], beats[-1]
        camera_line = ' '.join(l for l in last.splitlines() if l.strip().startswith('运镜'))
        end_line = last.split('→', 1)[-1]
        camera_tail = re.split(r'[，。；]', camera_line.rstrip('。'))[-1] if camera_line else ''
        tail = ' '.join([lmove if not camera_line else '', camera_tail, end_line])
        moving = MOVING_TAIL.search(tail)
        if moving and not STILL_TAIL.search(camera_tail + ' ' + end_line):
            warnings.append(f'{clip.name}: 尾镜可能仍在运动（“{moving.group(0)}”）；最后约1秒应动作完成、镜头静止')
        if '固定' not in fmove:
            warnings.append(f'{clip.name}: 首镜运镜为 “{fmove}”；定位秒应为固定')
        segs = [s for s in split_segments(next((c for n, _, c in split_blocks(clip.body) if n == '具体情节'), '')) if s['full']]
        if segs and segs[0]['end'] - segs[0]['start'] > Decimal('1.5'):
            warnings.append(f"{clip.name}: 首段 {segs[0]['end'] - segs[0]['start']} 秒；定位秒约 1 秒，人物到位、不说台词、不做动作")
        rank = size_rank(fsize)
        if rank is not None and rank > 3:
            warnings.append(f'{clip.name}: 首镜是{fsize}；定位秒默认全景，按戏份可用中景')
        picture = ' '.join(l for l in first.splitlines() if l.strip().startswith('画面'))
        if not STATE_WORDS.search(picture or first[:160]):
            warnings.append(f'{clip.name}: 首镜画面未写人物位置/朝向/持物；定位秒需让画面先到位')
    for (prev, pb), (nxt, nb) in zip(rows, rows[1:]):
        if not pb or not nb:
            continue
        a, b = size_rank(pb[-1][0]), size_rank(nb[0][0])
        if a is not None and b is not None and abs(a - b) < 2 and not ANGLE_CHANGE.search(nb[0][0] + nb[0][2][:60]):
            warnings.append(f'{prev.name}→{nxt.name}: 尾镜{pb[-1][0]}与首镜{nb[0][0]}相近且未写换角度/换对象；边界应明显换镜头')
    return warnings + craft_warnings(text) + variety_warnings(text) + risk_warnings(text)



# Visual variety (template §1 镜头变化). WARN only: a 20 s+ clip that stays at
# one or two shot sizes, never moves, or repeats a size three times reads flat.
def variety_warnings(text: str) -> list[str]:
    warnings = []
    for clip in parse_clips(text):
        segs = [s for s in split_segments(next((c for n, _, c in split_blocks(clip.body) if n == '具体情节'), '')) if s['full']]
        if not segs:
            continue
        total = segs[-1]['end']
        ranks = [size_rank(s['size']) for s in segs]
        if total >= 20 and len({r for r in ranks if r is not None}) < 3:
            warnings.append(f'{clip.name}: {total} 秒只用了 {len({r for r in ranks if r is not None})} 种景别；20 秒以上建议至少 3 种（远/全/中/近/特写）')
        if total >= 20 and len({s['fov'] for s in segs}) < 3:
            warnings.append(f'{clip.name}: 视场角只用了 {len({s["fov"] for s in segs})} 档；20 秒以上建议至少 3 档')
        if total >= 20 and all(camera_kind(s['move'])[0] in (None, '固定') for s in segs):
            warnings.append(f'{clip.name}: {total} 秒全部是固定镜头；至少给一个有动机的运镜（推近、跟拍、揭示）')
        run = 1
        for a, b in zip(ranks, ranks[1:]):
            run = run + 1 if a is not None and a == b else 1
            if run == 3:
                warnings.append(f'{clip.name}: 连续 3 段同一景别；换景别或换角度，或合并成一段')
                break
    return warnings


# Generation risks (template §1 生成风险). WARN only; each has a fallback.
WORDS_PER_SECOND = Decimal('2.5')  # natural English speech, screening only


def risk_warnings(text: str) -> list[str]:
    warnings = []
    for clip in parse_clips(text):
        blocks = {n: c for n, _, c in split_blocks(clip.body)}
        people = re.search(r'恰好\s*(\d+)\s*人', blocks.get('角色', ''))
        in_frame = re.search(r'最多\s*(\d+)\s*人入画', blocks.get('角色', ''))
        if people and int(people.group(1)) >= 5 and not (in_frame and int(in_frame.group(1)) <= 3):
            warnings.append(f'{clip.name}: 同框 {people.group(1)} 人，模型容易混脸或丢人；多人镜头尽量 ≤3 人入画，其余人用背影或出画，并在 [角色] 写“每次最多 3 人入画”')
        for line in audio_lines(blocks.get('声音', '')):
            label = f"{clip.name} {line['start']}s-{line['end']}s"
            length = line['end'] - line['start']
            words = len(re.findall(r"[A-Za-z']+", line['text']))
            if words and length > 0 and Decimal(words) / WORDS_PER_SECOND > length:
                warnings.append(f'{label}: 台词 {words} 个词约需 {(Decimal(words) / WORDS_PER_SECOND).quantize(Decimal("0.1"))} 秒，超过本行 {length} 秒；加长时间段或拆开')
        for seg in split_segments(blocks.get('具体情节', '')):
            if not seg['full']:
                continue
            label = f"{clip.name} {seg['start']}s-{seg['end']}s"
            picture = ' '.join(seg['fields'].get('画面', []))
            if re.search(r'屏幕里|屏幕中|取景框里|画面里的画面|镜子里|倒影里', picture):
                warnings.append(f'{label}: 画中画（屏幕/镜子/倒影里的人物）容易出错；备选：只拍屏幕的光照在脸上，或切到被拍的人')
    return warnings


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
    for warning in boundary_warnings(args.file.read_text(encoding='utf-8-sig')):
        print(f'WARN: {warning}')
    print(f'{"FAIL" if failures else "PASS"}: {count} Clip；仅文本契约检查，语义/绑定/生成结果未验收。')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
