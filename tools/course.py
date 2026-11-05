#!/usr/bin/env python3
"""Validate the published-course catalog and generate the roadmap.

No third-party packages or network calls required.
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'data' / 'course_manifest.json'
ROADMAP = ROOT / 'ROADMAP.md'
MODULE_ORDER = [
    'AI and engineering foundations',
    'Large language models',
    'Knowledge-aware AI applications',
    'Advanced retrieval and AI agents',
    'Advanced AI applications',
    'Production AI engineering',
]


def load():
    with MANIFEST.open(encoding='utf8') as fp:
        return json.load(fp)


def validate(data):
    errors=[]
    lessons=data.get('lessons',[])
    if len(lessons)!=90:
        errors.append(f'Expected 90 lessons, found {len(lessons)}.')
    if data.get('release_days')!=30 or data.get('lessons_per_day')!=3:
        errors.append('Release dimensions must be 30 days × 3 lessons.')
    seen=set(); published_paths=set(); expected_paths=set()
    for index, l in enumerate(lessons):
        day=index//3+1; no=index%3+1
        expected_id=f'D{day:02}L{no:02}'
        lid=l.get('id','')
        if lid!=expected_id: errors.append(f'At ordinal {index+1}: expected {expected_id}, got {lid}.')
        if lid in seen: errors.append(f'Duplicate ID {lid}.')
        seen.add(lid)
        if l.get('day')!=day or l.get('lesson')!=no:
            errors.append(f'{lid}: wrong day or lesson index.')
        prev=lessons[index-1]['id'] if index>0 else None
        nxt=lessons[index+1]['id'] if index<len(lessons)-1 else None
        if l.get('previous_id')!=prev or l.get('next_id')!=nxt:
            errors.append(f'{lid}: broken previous/next chain.')
        if not l.get('title') or l.get('module') not in MODULE_ORDER:
            errors.append(f'{lid}: missing title or invalid module.')
        target=l.get('expected_path','')
        if not re.fullmatch(r'course/day-\d\d-[a-z0-9-]+/\d\d-[a-z0-9-]+/README\.md',target):
            errors.append(f'{lid}: expected_path is not a safe lesson path: {target!r}')
        if target in expected_paths: errors.append(f'Duplicate expected path: {target}')
        expected_paths.add(target)
        status=l.get('status')
        if status not in ('planned','prepared','published'):
            errors.append(f'{lid}: status must be planned, prepared or published.')
        if status in ('planned','prepared') and l.get('guide_path') is not None:
            errors.append(f'{lid}: unreleased lesson must not have a live guide_path.')
        if status=='prepared':
            if not (ROOT / target).is_file():
                errors.append(f'{lid}: prepared local guide is missing: {target}')
            published_paths.add(target)  # Allowed local file; not a release claim.
        if status=='published':
            gp=l.get('guide_path')
            if gp!=target: errors.append(f'{lid}: published guide_path must equal expected_path.')
            if not (ROOT / target).is_file(): errors.append(f'{lid}: published guide is missing: {target}')
            published_paths.add(target)
    for p in (ROOT/'course').rglob('README.md'):
        relative=p.relative_to(ROOT).as_posix()
        if relative!='course/README.md' and relative not in published_paths:
            errors.append(f'Unlisted or unapproved public guide: {relative}')
    return errors


def render(data):
    lessons=data['lessons']
    total=sum(l['status']=='published' for l in lessons)
    out=[
        '# Complete Course Roadmap',
        '',
        f'**{total}/90 lessons published.** The full curriculum is planned; only linked lessons are live.',
        '',
        '> Three educational videos each release day. The 30 days are the publication schedule, **not** a promise of mastering AI engineering in 30 days.',
        '',
        'Every lesson is free, with its own visual GitHub guide when released. Learn at your own pace.',
        '',
        '[← Course homepage](README.md) · [Getting started](GETTING_STARTED.md)',
        '',
    ]
    for module_index,module in enumerate(MODULE_ORDER,1):
        out.extend([f'## Module {module_index}: {module}',''])
        module_lessons=[l for l in lessons if l['module']==module]
        out.append('| Day | Theme | Lesson 1 | Lesson 2 | Lesson 3 |')
        out.append('| --- | --- | --- | --- | --- |')
        for day in sorted({l['day'] for l in module_lessons}):
            three=[l for l in module_lessons if l['day']==day]
            def cell(l):
                txt=f"`{l['id']}` {l['title']}"
                if l['status']=='published':
                    txt=f"[{txt}]({l['guide_path']}) ✅"
                elif l['status']=='prepared':
                    txt+=' · *Prepared locally; unreleased*'
                else:
                    txt+=' · *Planned*'
                return txt.replace('|','\\|')
            row=[f'{day:02}',three[0]['day_theme'],*(cell(l) for l in three)]
            out.append('| '+' | '.join(row)+' |')
        out.append('')
    out.extend([
        '## Legend','',
        '- **Planned:** syllabus topic only; guide and Reel are not yet public.',
        '- **Prepared locally; unreleased:** local guide exists for review; no live URL or release approval is implied.',
        '- **✅ Published:** public lesson guide exists and is directly linked.',
        '',
        'Found an error? [See how to suggest a correction](CONTRIBUTING.md).',
        '',
        '<!-- Generated from data/course_manifest.json. Run: python tools/course.py roadmap -->',
        '',
    ])
    return '\n'.join(out)


def main():
    if len(sys.argv)!=2 or sys.argv[1] not in ('check','roadmap'):
        print('Usage: python tools/course.py {check|roadmap}')
        return 2
    data=load()
    errors=validate(data)
    if errors:
        for error in errors: print('ERROR:',error,file=sys.stderr)
        return 1
    desired=render(data)
    if sys.argv[1]=='roadmap':
        ROADMAP.write_text(desired,encoding='utf8')
        print(f'Regenerated ROADMAP.md ({sum(l["status"]=="published" for l in data["lessons"])}/90 published).')
    else:
        if not ROADMAP.exists() or ROADMAP.read_text(encoding='utf8')!=desired:
            print('ERROR: ROADMAP.md is out of date; run python tools/course.py roadmap',file=sys.stderr)
            return 1
        print('Public catalog, lesson IDs, navigation, files and ROADMAP.md: OK.')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
