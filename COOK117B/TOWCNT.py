def numden(x1, x2):
    return x2-x1


t = int(input())
for _ in range(t):
    ob = []
    h, n = map(int, input().split())
    for _ in range(n):
        obs = list(map(int, input().split()))
        ob.append(obs[1:]+obs[0:1])
    ob.sort()
    c = [0 for _ in range(n)]
    print(ob)
    for i in range(n-1):
        xi = ob[i][0]
        yi = ob[i][1]
        Mnum = float("inf")
        Mden = 1
        mnum = -float("inf")
        mden = 1
        for j in range(i+1, n):
            den, num = numden(xi, ob[j][0]), numden(yi, ob[j][1])
            if ob[j][-1] == 0:
                if (mnum * den < mden * num) and (Mnum * den > Mden * num):
                    c[i] += 1
                    c[j] += 1
                    mnum, mden = num, den
            else:
                if (mnum * den < mden * num) and (Mnum * den > Mden * num):
                    c[i] += 1
                    c[j] += 1
                    Mnum, Mden = num, den
    print(*c)
