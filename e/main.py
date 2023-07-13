import math

l, r = tuple(map(int, input().split()))

def num_mstrings(n):
    if n == 1:
        return 7
    if n == 2:
        return 7
    if n == 3:
        return 29

    if n % 2 == 0:
        return num_mstrings(n - 1)

    exp = math.floor(n / 2)

    return 5 ** exp + 2 ** exp

s = 0

for i in range(1, 200, 2):
    s += num_mstrings(i)
    print("%d %d"%(i, s))

