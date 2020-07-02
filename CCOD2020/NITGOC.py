t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x == 1 or y == 1:
        print("YES")
    elif x % y == 1 or y % x == 1:
        print("YES")
    else:
        print("NO")
