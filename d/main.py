a, b, c, d = tuple(map(int, input().split()))

count = 0

for i in range(a, b + 1):
    if i % c == 0 and i % d == 0:
        count += 1

print(count)
