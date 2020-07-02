d = set()


def q(r1, c1, r2, c2):
    d.add(" ".join(list(map(str, [r1, c1, r2, c2]))))
    if r2-r1 == 1 or c2-c1 == 1 or r2-r1 == 2 or c2-c1 == 2:
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if " ".join(list(map(str, [i, j, i, j]))) not in d:
                    q(i, j, i, j)
    else:
        print(1, r1, c1, r2, c2)
        x = int(input())
        if x == -1:
            quit()
        elif x == 0:
            return
        elif x == ((r2-r1)+1)*((c2-c1)+1):
            for i in range(r1-1, r2):
                for j in range(c1-1, c2):
                    m[i][j] = 1
        else:
            r3, c3 = (r1+r2)//2, (c1+c2)//2
            if " ".join(list(map(str, [r1, c1, r3, c3]))) not in d:
                q(r1, c1, r3, c3)
            if " ".join(list(map(str, [r3, c1, r2, c3]))) not in d:
                q(r3, c1, r2, c3)
            if " ".join(list(map(str, [r1, c3, r3, c2]))) not in d:
                q(r1, c3, r3, c2)
            if " ".join(list(map(str, [r3, c3, r2, c2]))) not in d:
                q(r3, c3, r2, c2)


t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    m = [[0 for i in range(n)] for i in range(n)]
    q(1, 1, n, n)

    print(2)
    for i in range(n):
        print(*m[i])
    x = int(input())
    if x == 1:
        continue
    else:
        break
