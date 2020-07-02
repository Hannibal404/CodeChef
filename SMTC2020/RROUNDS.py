from math import pi


t = int(input())
for _ in range(t):
    x, r, a, b = map(int, input().split())
    circ = 2 * pi * r
    totl = x * circ
    if a > b:
        ans = int((totl - (totl/a) * b)//circ)
        if a%b == 0:
            ans -=1
        print(ans)
    else:
        ans = int((totl - (totl/b) * a)//circ)
        if b%a == 0:
            ans -= 1
        print(ans)