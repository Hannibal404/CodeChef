t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,list(input())))
    ac=0
    bc=0
    x=0
    for i in range(2*n):
        if i%2==0:
            if a[i]==1:
                ac+=1
        if i%2!=0:
            if a[i]==1:
                bc+=1
        if i%2==0:
            if ac>bc+n-(i//2) or bc>ac+n-(i//2)-1:
                print(i+1)
                x=-1
                break
        if i%2!=0:
            if ac>bc+n-(i//2)-1 or bc > ac + n - (i//2) -1:
                print(i+1)
                x=-1
                break
    if x==0:
        print(2*n)