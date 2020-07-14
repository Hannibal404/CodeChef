t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n-1):
        s += abs(a[i+1]-a[i]) - 1
    print(s)
