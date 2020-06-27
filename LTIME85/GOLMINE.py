t = int(input())
for _ in range(t):
    n = int(input())
    s1, s2 = 0, 0
    for i in range(n):
        g, a, b = map(int, input().split())
        s1 += (b/(a+b)) * g
        s2 += (a/(a+b)) * g
    print(s1, s2)
