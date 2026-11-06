"""Variable-duration evidence regressions; no acting or speech simulation."""
import copy
from pathlib import Path
import re
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import shot_rhythm_lint as lint


def prompt(lengths,continuation=False):
    """Segments of given lengths; with continuation, segments after the first keep the same shot."""
    sys.path.insert(0,str(Path(__file__).resolve().parent))
    from studio_fixtures import prompt as build, segment
    cursor=0;segs=[]
    for i,duration in enumerate(lengths,1):
        end=cursor+duration
        size='中景' if (i==1 or continuation) else '切至中景'
        segs.append(segment(f'{cursor:g}',f'{end:g}',size,47,'固定',
            picture='母亲蹲在窝边，三只幼龙面向她，画面左侧是低芯灯。',camera='固定，平视。',
            action='母亲注视孩子。' if continuation and i>1 else '母亲完整说话，孩子注视听完。',
            expression='母亲眉眼放松，嘴角上扬。',end_state='母亲停住。'))
        cursor=end
    body=build(segs,goal='母亲告别孩子。',style='低芯灯，3200K。',consistency='母亲 1 人，幼龙 3 只。无字幕、无水印。')
    return '# Clip 1-1｜告别｜时长：'+str(cursor)+'秒\n```text\n'+body+'```\n'


def evidence(text):
    errors,warnings,shots=lint.validate(text)
    return dict(file_sha256=lint.digest(text),shots=[dict(clip_id=s['clip_id'],shot_id=s['shot_id'],time_range_seconds=[s['start'],s['end']],content_sha256=s['content_sha256'],watch_task='完整观察母亲目光交给孩子，孩子听懂才回应。',timing_basis='文字估算：完整叮嘱与气口占用4秒，待自然朗读和样片校准。',cut_reason='叮嘱末句与目光交接结束后切到孩子的同意回应。') for s in shots],equal_run_reviews=[])


class RhythmTests(unittest.TestCase):
    def test_long_shot_is_warning_not_hard_failure(self):
        errors,warnings,_=lint.validate(prompt([4,2]))
        self.assertEqual(errors,[]);self.assertTrue(any('长镜复核' in w for w in warnings))

    def test_long_shot_strict_evidence_can_pass(self):
        text=prompt([4,2]);self.assertEqual(lint.validate(text,evidence(text),True)[0],[])
        self.assertTrue(lint.validate(text,None,True)[0])

    def test_missing_long_row_fails(self):
        text=prompt([4,2]);review=evidence(text);review['shots']=[]
        self.assertTrue(any('缺少长镜' in e for e in lint.validate(text,review,True)[0]))

    def test_full_hash_content_range_and_cliche_drift_are_rejected(self):
        text=prompt([4,2]);baseline=evidence(text)
        for field,value in [('file_sha256','old'),('content_sha256','old'),('time_range_seconds',[0,3]),('cut_reason','凑30秒'),('timing_basis','对白未完')]:
            review=copy.deepcopy(baseline)
            if field=='file_sha256':review[field]=value
            else:review['shots'][0][field]=value
            with self.subTest(field=field):self.assertTrue(lint.validate(text,review,True)[0])

    def test_equal_run_warns_but_is_not_randomized_or_failed(self):
        text=prompt([3,3,3,3]);errors,warnings,_=lint.validate(text)
        self.assertEqual(errors,[]);self.assertTrue(any('等长镜头复核' in w for w in warnings))
        review=evidence(text)
        self.assertTrue(lint.validate(text,review,True)[0])
        review['equal_run_reviews']=[dict(clip_id='1-1',shot_ids=[1,2,3,4],reason='四镜对应同一重复仪式节拍，逐项核查观察任务和动作窗口后保留等长。')]
        self.assertEqual(lint.validate(text,review,True)[0],[])

    def test_varied_lengths_do_not_require_equal_run_review(self):
        text=prompt([2,4,2.5,3.5]);errors,warnings,_=lint.validate(text,evidence(text),True)
        self.assertEqual(errors,[]);self.assertFalse(any('等长' in w for w in warnings))

    def test_same_shot_rows_accumulate_without_cut_word(self):
        text=prompt([2,2],True);_,warnings,shots=lint.validate(text)
        self.assertEqual(len(shots),1);self.assertEqual(shots[0]['duration'],4)
        self.assertTrue(any('长镜' in w for w in warnings))

    def test_stage_without_cut_word_continues_the_shot(self):
        text=prompt([2,2]).replace('2s-4s｜切至中景｜','2s-4s｜中景｜')
        _,_,shots=lint.validate(text)
        self.assertEqual(len(shots),1)
        self.assertEqual(shots[0]['duration'],4)

    def test_cut_word_starts_a_new_shot(self):
        shots=lint.extract_shots(prompt([2,2]))
        self.assertEqual([s['shot_id'] for s in shots],[1,2])

    def test_clip_hard_limit_is_not_relaxed(self):
        text=prompt([31]);self.assertTrue(any('30秒' in e for e in lint.validate(text)[0]))

    def test_extra_duplicate_review_rows_fail(self):
        text=prompt([4,2]);review=evidence(text);review['shots'].append(copy.deepcopy(review['shots'][0]))
        self.assertTrue(any('重复' in e for e in lint.validate(text,review,True)[0]))

    def test_scoped_review_ignores_other_clip_warnings_not_structure(self):
        text=prompt([4,2]);other=prompt([3,3,3,3]).replace('Clip 1-1','Clip 1-2');combined=text+other
        review=evidence(text);review.update(file_sha256=lint.digest(combined),scope=['1-1'])
        self.assertEqual(lint.validate(combined,review,True,['1-1'])[0],[])
        self.assertTrue(lint.validate(combined,review,True,['1-2'])[0])
        self.assertTrue(lint.validate(combined,review,True,['1-99'])[0])


if __name__=='__main__':unittest.main()
