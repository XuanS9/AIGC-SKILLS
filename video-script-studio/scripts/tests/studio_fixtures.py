"""Shared studio-format fixtures: Higgsfield blocks in Chinese, [具体情节] segments, English dialogue."""


def segment(start, end, size, fov, move, *, picture, camera, action, expression,
            listener=None, sound=None, end_state):
    lines = [f'{start}s-{end}s｜{size}｜视场角{fov}°｜{move}',
             f'画面：{picture}', f'运镜：{camera}', f'动作：{action}', f'表情：{expression}']
    if listener:
        lines.append(f'听者：{listener}')
    if sound:
        lines.append(f'声音：{sound}')
    lines.append(f'→ 结束：{end_state}')
    return '\n'.join(lines)


def prompt(segments, *, characters=None, props=None, scenes=None, goal='她在柜台旁递还钥匙，对方接住。',
           style='侧窗柔光从画面左侧射入，色温 4000K，玻璃反光低对比。', cut=True,
           audio='本段无对白（设计）。现场声为房间底噪。NO BGM。',
           consistency='钥匙始终只有 1 把。左右均以镜头为准。无字幕、无水印。'):
    blocks = []
    if characters is not None:
        blocks.append('[角色]\n' + characters)
    if props is not None:
        blocks.append('[道具]\n' + props)
    if scenes is not None:
        blocks.append('[场景]\n' + scenes)
    blocks.append('[生成目标]\n' + goal)
    blocks.append('[具体情节]\n' + '\n\n'.join(segments))
    blocks.append('[视觉风格]\n' + style)
    camera = '各段视场角段内不漂移，一段只做一个主运动。'
    if cut:
        camera += '只在指定处切镜，镜头不会自行切换。'
    blocks.append('[镜头]\n' + camera)
    blocks.append('[声音]\n' + audio)
    blocks.append('[保持一致]\n' + consistency)
    return '\n\n'.join(blocks) + '\n'


KEY_SEGMENTS = [
    segment('0', '2.5', '侧面中景', 47, '固定',
            picture='柜台横在画面中部，她站在画面左，对方站在画面右。',
            camera='固定，平视，不推拉。',
            action='她右手捏住钥匙环，把钥匙递到柜台中央，指尖仍勾着环。',
            expression='她目光落在钥匙上，嘴唇抿紧。',
            sound='<钥匙轻触玻璃>。',
            end_state='钥匙仍在她指间。'),
    segment('2.5', '5', '切至双手近景', 29, '固定',
            picture='柜台台面占满画面，两只手从画面左右进入。',
            camera='固定，俯角约 30°，对焦在钥匙上。',
            action='对方手掌托住钥匙，她才松开手指。',
            expression='她的指尖微微发抖，呼吸放浅，随后手指收拢。',
            end_state='她的右手收回柜台外缘，钥匙在对方掌心。'),
]

KEY = prompt(KEY_SEGMENTS)


def fenced(body=KEY, name='1-1', duration='5'):
    return f'# Clip {name}｜归还钥匙\n时长：{duration}秒\n```text\n{body}```\n'


def audio(*lines, ambience='现场声为房间底噪。'):
    """[声音] content: dialogue lines are '起s-止s｜说话人＋状态＋说：{line}' (Higgsfield)."""
    if not lines:
        return f'本段无对白（设计）。{ambience}NO BGM。'
    return '对白语言：英语。\n' + '\n'.join(lines) + f'\n{ambience}NO BGM。'


HM = '0s-2.5s｜她轻声：{Hm.}'


def with_dialogue(body=KEY, line='Here you go.'):
    return body.replace('本段无对白（设计）。', f'对白语言：英语。\n2.5s-5s｜她压低气音说：{{{line}}}\n')
