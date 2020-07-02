def lcal(inp):
    c = "CONTEST_WON"
    t = "TOP_CONTRIBUTOR"
    b = "BUG_FOUND"
    ch = "CONTEST_HOSTED"

    if t in inp:
        return 300
    if ch in inp:
        return 50
    if c in inp:
        r = int(inp.split()[1])
        if r<21:
            return 320 - r
        return 300
    if b in inp:
        return int(inp.split()[1])


t = int(input())
for _ in range(t):
    ai = input().split()
    n = int(ai[0])
    if ai[1] == "INDIAN":
        ind = True
    else:
        ind = False
    xan = 0
    for i in range(n):
        xan += lcal(input())
    if ind:
        print(xan//200)
    else:
        print(xan//400)