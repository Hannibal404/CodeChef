t = int(input())
for _ in range(t):
    n, = map(int, input().split())
    a = list(map(int, input().split()))
    c, k = 1, 1
    b = []
    s=set()
    for i in a:
        b.append(i)
        s.add(i)
    dic = {}
    for i in s:
        k+=1
        dic[i] = k
    M = k-1
    