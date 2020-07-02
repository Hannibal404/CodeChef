t = int(input())
for _ in range(t):
    n,b,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = 1
    minr = a[0]//b

    for i in range(1,m):
        if minr == a[i]//b:
            continue
        else:
            c += 1
            minr = a[i]//b

    print(c)