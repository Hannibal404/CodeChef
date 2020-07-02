from math import sqrt

def dist(x,y):
    return sqrt((x**2)+(y**2))
t = int(input())
for _ in range(t):
    xa,ya,xb,yb = map(int,input().split())
    da = dist(xa,ya)
    db = dist(xb,yb)
    if da>=db:
        print("A IS CLOSER")
    else:
        print("B IS CLOSER")