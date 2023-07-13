n = int(input())
hotels = list(map(int, input().split()))

hits = 0

for i in range(1, 7):
    for j in range(1, 7):
        s = i + j

        if s in hotels:
            hits += 1

print(hits / 36)
