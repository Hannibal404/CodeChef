t = int(input())
for _ in range(t):
    n, = map(int, input().split())
    a = list(map(int, input().split()))
    dic = {}
    dic[a[0]] = 1
    r = a[0]
    for i in range(1, n):
        if a[i] != r:
            if a[i] in dic.keys():
                dic[a[i]] += 1
            else:
                dic[a[i]] = 1
            r = a[i]
        else:
            r = - 1

    ans = float("inf")
    m = -1
    for i in dic.keys():
        if dic[i] > m and i < ans:
            ans = i
            m = dic[i]
    print(ans)
