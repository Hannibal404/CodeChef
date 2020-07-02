t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        m = [[0]]
    else:
        m = [[0 for i in range(n)] for j in range(n)]
        for i in range(0, n, 2):
            pre = (i * n) + 1
            for j in range(n):
                m[i][j] = pre + j
        for i in range(1, n, 2):
            pre = (i+1)*n
            for j in range(n):
                m[i][j] = pre - j
    for i in range(n):
        print(*m[i])
