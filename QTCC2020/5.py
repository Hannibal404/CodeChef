t = int(input())
for _ in range(t):
    th, tl, nh, nl = map(int, input().split())
    av = th + tl - (nh + nl)
    av /= 2
    if av > 0:
        print("%0.1f" % av, "DEGREE(S) ABOVE NORMAL")
    else:
        print("%0.1f" % abs(av), "DEGREE(S) BELOW NORMAL")
