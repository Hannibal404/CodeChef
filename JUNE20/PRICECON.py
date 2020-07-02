t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    l = 0
    for i in a:
        if i > k:
            l += (i-k)
    print(l)
