def nzero(n):
    c=0
    x=5
    while x<=n:
        c+=n//x
        x*=5
    return c
t=int(input())
for i in range(t):
    print(nzero(int(input())))