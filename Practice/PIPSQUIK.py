t = int(input())
for _ in range(t):
    n, h, y1, y2, l = map(int, input().split())
    b = []
    dh = h-y1
    for _ in range(n):
        b.append(list(map(int, input().split())))
    bn = 0
    i = 0
    while i < n:
        x = b[i][1]
        if b[i][0] == 1:
            if x >= dh:
                bn += 1
            else:
                if l == 1:
                    break
                else:
                    bn += 1
                    l -= 1
        else:
            if x <= y2:
                bn += 1
            else:
                if l == 1:
                    break
                else:
                    bn += 1
                    l -= 1
        i += 1
    print(bn)
