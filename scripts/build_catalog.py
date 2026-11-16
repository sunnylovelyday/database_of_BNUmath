"""Generate a static catalog from tracked resource files; no runtime GitHub API needed."""
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
CATEGORIES = {'考试题目', '教材答案', '其他资料'}

def build(paths):
    result = []
    for name in paths:
        path = pathlib.PurePosixPath(name)
        if path.parts[0] not in CATEGORIES or any(p.startswith('.') for p in path.parts):
            continue
        local = ROOT / path
        if not local.is_file():
            continue
        result.append(dict(path=name, name=path.name, category=path.parts[0],
                           course=path.parts[1] if path.parts[0] == '考试题目' and len(path.parts) > 2 else '',
                           size=local.stat().st_size))
    return sorted(result, key=lambda x: x['path'])

if __name__ == '__main__':
    paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
    files = build([p for p in paths if p])
    (ROOT / 'catalog.json').write_text(json.dumps(files, ensure_ascii=False), encoding='utf-8')
    print(f'Indexed {len(files)} resources')
