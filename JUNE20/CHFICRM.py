t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = {5: 0, 10: 0, 15: 0}
    f = True
    if a[0] != 5:
        print("NO")
        continue
    else:
        d[5] += 1
        for i in range(1, n):
            if a[i] == 5:
                d[5] += 1
            elif a[i] == 10:
                d[10] += 1
                if d[5] > 0:
                    d[5] -= 1
                else:
                    f = False
                    break
            else:
                d[15] += 1
                if d[10] > 0:
                    d[10] -= 1
                elif d[5] > 1:
                    d[5] -= 2
                else:
                    f = False
                    break
        if f:
            print("YES")
        else:
            print("NO")
