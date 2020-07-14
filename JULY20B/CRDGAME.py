def cardpower(x):
    pow = 0
    while x > 0:
        pow += x % 10
        x //= 10
    return pow


t = int(input())
for _ in range(t):
    n = int(input())
    pntm, pntc = 0, 0
    for i in range(n):
        powc, powm = map(cardpower, map(int, input().split()))
        if powc > powm:
            pntc += 1
        elif powc < powm:
            pntm += 1
        else:
            pntc += 1
            pntm += 1
    if pntm == pntc:
        print(2, pntc)
    elif pntc > pntm:
        print(0, pntc)
    else:
        print(1, pntm)
