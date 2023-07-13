import sys

words = [x.rstrip() for x in sys.stdin.readlines()][1:]

print(words)

def solve():
    for word in words:
        if len(set(word)) < 3:
            print("0")
            return

    if len(set("".join(words))) > 18:
        print("0")
        return

    res1 = set()
    res2 = set()
    res3 = set()

    for w in words:
        ls = [x for x in w]

        if 



    print(res1)
    print(res2)
    print(res3)





    

solve()

