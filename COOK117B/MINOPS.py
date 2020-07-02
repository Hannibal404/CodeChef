t = int(input())
for _ in range(t):
    r = input()
    s = input()
    n = len(r)
    l = 1
    k = 1
    i = 0
    rep = []
    while i < n:
        if r[i] == s[i]:
            i += 1
        else:
            break
    st = i
    while i < n:
        if r[i] != s[i]:
            l += 1
            rep.append(i - st - 1)
            st = i
        i += 1
    k = l
    rep.sort()
    ans = (k*l)
    for i in range(len(rep)):
        k -= 1
        l += rep[i]
        ans = min(ans, k*l)
    print(ans)
