t=int(input())
for _ in range(t):
    n=int(input())
    x=int(input())
    a=list(map(int,input().split()))
    a.sort()
    y=0
    i=0
    a1=x*i
    while a1 < n:
        if a1+x <=n:
            if min(a[a1:a1+x])-i<=1:
                print("Impossible")
                y=-1
                break
        else:
            if min(a[a1:])-i <= 1:
                y=-1
                print("Impossible")
                break
        i+=1
        a1+=x
    if y==0:
        print("Possible")