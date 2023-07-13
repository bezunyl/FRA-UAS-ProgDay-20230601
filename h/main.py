import sys

lines = [x.rstrip() for x in sys.stdin.readlines()]

t, b = tuple(map(int, lines[0].split()))
packtype = list(map(int, lines[1].split()))

lines = lines[2:]

latest_lines = lines[:t]

latest = {}

for line in latest_lines:
    line = line.split()
    name = line[0]
    version = int(line[1])

    latest[name] = version

current_lines = lines[t:]

pointer = 0

for i, s in enumerate(packtype):
    delta = 0

    rel = current_lines[pointer:pointer + s]

    for r in rel:
        r_s = r.split()

        name = r_s[0]
        version = int(r_s[1])

        delta += latest[name] - version

    pointer += s

    print(delta)
