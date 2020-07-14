t = int(input())
for _ in range(t):
    n = int(input())
    x, y = set(), set()
    for i in range((4*n)-1):
        x1, y1 = map(int, input().split())
        if x1 in x:
            x.remove(x1)
        else:
            x.add(x1)
        if y1 in y:
            y.remove(y1)
        else:
            y.add(y1)
    for i in x:
        print(i, end=" ")
    for j in y:
        print(j)
