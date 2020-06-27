t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    f = [0 for i in range(30)]

    for i in a:
        s = bin(i)[2:]
        l = len(s)
        for j in range(l):
            if s[j] == '1':
                f[l-1-j] += 1

    val = []
    for i, j in enumerate(f):
        val.append(j*(2**i))

    val = sorted(zip(val, range(30)), key=lambda x: x[0], reverse=True)
    print(val)
    if k == 1:
        print(2**val[0][1])
    elif k == 2:
        print(2**val[0][1]+2**val[1][1])
    else:
        out = 0
        for i in range(k):
            out += 2**val[i][1]
        print(out)
