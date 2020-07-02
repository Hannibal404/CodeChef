t = int(input())
for _ in range(t):
    n = int(input())
    food = []
    for _ in range(n):
        food.append(list(map(int, input().split())))
    p = (food[0][1]//(food[0][0]+1)) * food[0][2]
    if n > 1:
        for i in range(n):
            tp = (food[i][1]//(food[i][0]+1)) * food[i][2]
            if tp > p:
                p = tp
    print(p)
