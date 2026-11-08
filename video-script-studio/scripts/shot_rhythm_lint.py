#!/usr/bin/env python3
"""Review shot timing without imposing a fixed shot length.

3 seconds triggers review, not a hard failure. Equal runs trigger a warning.
Strict mode checks hash-bound review evidence, not acting or cut semantics.
Four-section and <=30s Clip constraints remain in director_contract_lint.
"""
from __future__ import annotations
import argparse
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import sys
import director_contract_lint as contract

REVIEW_THRESHOLD = Decimal(3)
MIN_EQUAL_RUN = 4
# Each [具体情节] segment "0s-3s｜景别｜视场角N°": a segment whose shot size opens
# with a cut word ("切至…") starts a new shot; any other segment continues the
# current shot (one continuous take across segments).
CUT_OPEN = re.compile(r'^(?:切至|切到|切回|硬切|反打|甩镜)')
EMPTY_REASONS = {'情绪需要','对白未完','凑30秒','保持电影感','超过3秒','同意','已复核'}


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def reason_valid(value):
    return isinstance(value,str) and len(value.strip())>=12 and value.strip().rstrip('。.!！') not in EMPTY_REASONS


def extract_shots(text):
    """One shot per segment that opens with a cut word; other segments continue the shot."""
    result=[]
    for clip in contract.parse_clips(text):
        scene=next((c for n,_,c in contract.split_blocks(clip.body) if n=='具体情节'),'')
        local=[]
        for seg in contract.split_segments(scene):
            size,move=seg['size'],seg['move']
            start,finish=seg['start'],seg['end']
            opens_cut=bool(CUT_OPEN.match(size))
            same=local and not opens_cut
            label=f'{size}，{move}：{seg["raw"]}'
            if same:
                local[-1]['end']=float(finish)
                local[-1]['duration']=float(finish-Decimal(str(local[-1]['start'])))
                local[-1]['content']+='\n'+label
            else:
                sid=(local[-1]['shot_id']+1) if local else 1
                local.append(dict(clip_id=clip.name,shot_id=sid,start=float(start),end=float(finish),duration=float(finish-start),content=label))
        for shot in local:
            shot['content_sha256']=digest(shot['content'])
        result.extend(local)
    return result


def validate(text,review=None,strict_review=False,clip_ids=None):
    errors,_=contract.check_document(text)
    shots=extract_shots(text)
    if clip_ids is not None:
        known={c.name for c in contract.parse_clips(text)}
        if not set(clip_ids).issubset(known):errors.append('节奏复核Clip范围不存在')
        shots=[s for s in shots if s['clip_id'] in clip_ids]
    long=[s for s in shots if Decimal(str(s['duration']))>REVIEW_THRESHOLD]
    runs=[]
    for clip_id in dict.fromkeys(s['clip_id'] for s in shots):
        local=[s for s in shots if s['clip_id']==clip_id];a=0
        while a<len(local):
            z=a+1
            while z<len(local) and local[z]['duration']==local[a]['duration']:z+=1
            if z-a>=MIN_EQUAL_RUN:runs.append(dict(clip_id=clip_id,shot_ids=[s['shot_id'] for s in local[a:z]],duration=local[a]['duration']))
            a=z
    warnings=[f"长镜复核 {s['clip_id']}/{s['shot_id']}：{s['duration']:g}秒；非3秒硬上限" for s in long]
    warnings += [f"等长镜头复核 {r['clip_id']}：连续镜{r['shot_ids']}均{r['duration']:g}秒；不要随机改秒数" for r in runs]
    if review is not None:
        if not isinstance(review,dict):return errors+['节奏复核记录须为JSON对象'],warnings,shots
        if review.get('file_sha256')!=digest(text):errors.append('节奏复核全文哈希漂移')
        if clip_ids is not None and review.get('scope')!=list(clip_ids):errors.append('节奏复核声明范围漂移')
        entries=review.get('shots',[])
        if not isinstance(entries,list):errors.append('shots复核记录须为列表');entries=[]
        by={};actual={(s['clip_id'],s['shot_id']):s for s in shots}
        for entry in entries:
            if not isinstance(entry,dict):errors.append('非法镜头复核记录');continue
            key=(entry.get('clip_id'),entry.get('shot_id'))
            if key in by:errors.append('镜头复核记录重复：'+str(key))
            by[key]=entry
            if key not in actual:errors.append('镜头复核记录范围漂移：'+str(key));continue
            shot=actual[key]
            if entry.get('time_range_seconds')!=[shot['start'],shot['end']] or entry.get('content_sha256')!=shot['content_sha256']:errors.append('镜头复核区间/镜文哈希漂移：'+str(key))
            if not all(reason_valid(entry.get(field)) for field in ('watch_task','timing_basis','cut_reason')):errors.append('缺少具体观看/估时/切点依据：'+str(key))
        for shot in long:
            if (shot['clip_id'],shot['shot_id']) not in by:errors.append('缺少长镜复核记录：'+str((shot['clip_id'],shot['shot_id'])))
        equal=review.get('equal_run_reviews',[])
        if not isinstance(equal,list):errors.append('等长镜头复核记录须为列表');equal=[]
        for run in runs:
            matched=[e for e in equal if isinstance(e,dict) and e.get('clip_id')==run['clip_id'] and e.get('shot_ids')==run['shot_ids'] and reason_valid(e.get('reason'))]
            if len(matched)!=1:errors.append('缺少或重复等长镜头复核结论：'+str(run))
        for entry in equal:
            if not isinstance(entry,dict) or not any(entry.get('clip_id')==r['clip_id'] and entry.get('shot_ids')==r['shot_ids'] for r in runs):errors.append('等长镜头复核范围漂移')
    elif strict_review and (long or runs):
        errors.append('节奏复核记录缺失：长镜/等长警告须绑定当前文本')
    return errors,warnings,shots


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--file',type=Path,required=True)
    p.add_argument('--review',type=Path)
    p.add_argument('--clip',action='append',dest='clip_ids',help='限定本轮Clip，可重复；记录scope须一致')
    p.add_argument('--strict-review',action='store_true')
    p.add_argument('--report',type=Path)
    args=p.parse_args()
    try:
        text=args.file.read_text();review=json.loads(args.review.read_text()) if args.review else None
        errors,warnings,shots=validate(text,review,args.strict_review,args.clip_ids)
    except (OSError,ValueError,TypeError,KeyError) as e:
        print('INPUT ERROR: '+str(e),file=sys.stderr);return 2
    if args.report:args.report.write_text(json.dumps(dict(state='failed' if errors else 'passed_text_only',errors=errors,warnings=warnings,shots=shots,scope='文字结构及复核证据；不是表演/剪接实测'),ensure_ascii=False,indent=2)+'\n')
    for message in warnings:print('WARN: '+message)
    for message in errors:print('FAIL: '+message)
    print(('FAIL' if errors else 'PASS')+'：变长镜头复核；未验证真实表演/口型/剪接。')
    return bool(errors)


if __name__=='__main__':sys.exit(main())
