t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int,input().split()))
    min = n
    max = 0
    i = 0
    c = 1
    while i < n - 1:
        if x[i+1]-x[i]<=2:
            c += 1
        else:
            if c>max:
                max = c
            if c<min:
                min = c
            c=1
        i += 1
    if c>max:
        max = c
    if c<min:
        min = c
    print(min,max)