t=int(input())
for i in range(t):
    n=int(input())
    mcar=1
    cl=list(map(int,input().split()))
    i=1
    mspeed=cl[0]
    while i<n:
        if cl[i]<=mspeed:
            mcar+=1
            mspeed=cl[i]
        i+=1
    print(mcar)