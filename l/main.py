n = int(input())
pref = input()

l = list()

done = False

for i in range(n):
    port, size = tuple(map(int, input().split()))

    l.append((i + 1, port, size, port + size))

m = max(map(lambda x: x[3], l))

ms = list(filter(lambda x: x[3] == m, l))

if len(ms) == 1:
    print(ms[0][0])
    done = True

if not done:
    if pref == "antal":
        m_pref = max(map(lambda x: x[1], ms))
        ms_pref = list(filter(lambda x: x[1] == m_pref, ms))
        print(ms_pref[0][0])

    elif pref == "storlek":
        m_pref = max(map(lambda x: x[2], ms))
        ms_pref = list(filter(lambda x: x[2] == m_pref, ms))
        print(ms_pref[0][0])
