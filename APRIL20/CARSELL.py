t = int(input())
for i in range(t):
    n = int(input())
    cl = list(map(int, input().split()))
    cl.sort()
    cl.reverse()
    p=0
    i=0
    while cl[i]-i>0:
        p+=cl[i]-i
        i+=1
    print(p%(1000000007))