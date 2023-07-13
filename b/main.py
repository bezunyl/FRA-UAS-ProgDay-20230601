n = int(input())
nums = input().split()
number = input()
trans = {}

for i in range(n):
    trans[nums[i]] = i

number_s = []

p = 0
for i, c in enumerate(number):
    sub = number[p:i]

    if sub in nums:
        number_s.append(sub)
        p = i

number_s.append(number[p:])

conv = list(map(lambda x: trans[x], number_s))

conv.reverse()

res = 0

for i, c in enumerate(conv):
    res += (n ** i) * c

print(res)
