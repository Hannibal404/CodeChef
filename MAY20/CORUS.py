t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    s = input()
    d = {}
    for i in s:
        if ord(i) - 96 in d.keys():
            d[ord(i) - 96] += 1
        else:
            d[ord(i) - 96] = 1
    keys = set(d.keys())
    for i in range(q):
        cen = int(input())
        qs = 0
        for i in keys:
            if d[i] > cen:
                qs += d[i]-cen
        print(qs)
