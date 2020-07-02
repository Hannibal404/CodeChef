t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    m = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            print(1, i+1, j+1, i+1, j+1)
            x = int(input())
            if x == -1:
                quit()
            elif x == 1 :
                m[i][j] = 1
    print(2)
    for i in range(n):
        print(*m[i])
    x = int(input())
    if x == 1:
        continue
    else:
        break