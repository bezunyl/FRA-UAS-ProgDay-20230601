d, m, y = tuple(map(int, input().split("/")))

if d > 12 and m <= 12:
    print("EU")
elif d <= 12 and m > 12:
    print("US")
else:
    print("either")
