t = int(input())
for _ in range(t):
    n, = map(int,input().split())
    i = 1
    while n > i+1:
        n-= i+1
        i += 1
    print(n-1) 