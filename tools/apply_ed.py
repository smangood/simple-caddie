import re, sys
# Minimal applier for `diff -e` scripts (commands are bottom-up, so line numbers stay valid).
src, script, out = sys.argv[1:4]
lines = open(src, encoding="utf-8").read().split("\n")
cmds = open(script, encoding="utf-8").read().split("\n")
i = 0
while i < len(cmds):
    c = cmds[i]; i += 1
    if not c:
        continue
    m = re.fullmatch(r"(\d+)(?:,(\d+))?([acd])", c)
    if not m:
        sys.exit("bad command: " + c)
    a = int(m.group(1)); b = int(m.group(2) or a); op = m.group(3)
    text = []
    if op in "ac":
        while cmds[i] != ".":
            text.append(cmds[i]); i += 1
        i += 1
    if op == "a":
        lines[a:a] = text
    else:
        lines[a - 1:b] = text
open(out, "w", encoding="utf-8").write("\n".join(lines))
