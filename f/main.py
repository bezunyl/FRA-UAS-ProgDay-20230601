from itertools import groupby
s = input().split()
print(" ".join(map(lambda x: "".join([l for l, _ in groupby(x)]), s)))

