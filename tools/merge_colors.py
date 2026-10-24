"""Merge mod colour blocks onto a newer vanilla colors.txt / cosmetic.txt.
Vanilla layout is kept; any top-level KEY = { ... } the mod defines replaces vanilla's,
mod-only keys are appended. Usage: merge_colors.py vanilla mod out"""
import re, sys

def blocks(text):
    """Return {key: (start, end)} for top-level `KEY = { ... }` spans, skipping # comments."""
    out, depth, i, start, key = {}, 0, 0, None, None
    while i < len(text):
        c = text[i]
        if c == '#':
            i = text.find('\n', i)
            if i == -1: break
            continue
        if depth == 0:
            assert c != '}', f'stray }} at char {i}'
            m = re.compile(r'([A-Za-z0-9_]+)\s*=\s*\{').match(text, i)
            if m:
                key, start, depth, i = m.group(1), i, 1, m.end()
                continue
        elif c == '{': depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                out.setdefault(key, []).append((start, i + 1))  # vanilla has dupes, e.g. SOV_ROME
        i += 1
    assert depth == 0, 'unbalanced braces'
    return out

vanilla = open(sys.argv[1], encoding='utf-8-sig').read()
mod = open(sys.argv[2], encoding='utf-8-sig').read()
vb, mb = blocks(vanilla), blocks(mod)

def mod_text(key, n):  # n-th mod definition of key, falling back to its last one
    spans = mb[key]
    return mod[slice(*spans[min(n, len(spans) - 1)])]

res, pos = [], 0
for s, e, key, n in sorted((s, e, k, n) for k, sp in vb.items() for n, (s, e) in enumerate(sp)):
    res.append(vanilla[pos:s])
    res.append(mod_text(key, n) if key in mb else vanilla[s:e])
    pos = e
res.append(vanilla[pos:])
extra = [k for k in mb if k not in vb]
for k in extra:
    res.extend('\n' + mod[slice(*sp)] + '\n' for sp in mb[k])
merged = ''.join(res)

# self-check: every mod block survives verbatim, every vanilla key is still present
mm = blocks(merged)
assert all(merged[slice(*mm[k][-1])] == mod[slice(*mb[k][-1])] for k in mb)
assert set(vb) <= set(mm)
open(sys.argv[3], 'w', encoding='utf-8', newline='').write(merged)
print(f'{sys.argv[3]}: vanilla {len(vb)}, mod {len(mb)}, overridden {len(set(mb) & set(vb))}, mod-only {extra}')
