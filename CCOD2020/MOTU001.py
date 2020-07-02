t=int(input())
for _ in range(t):
    a , b, c= map(int,input().split())
    q=c//a
    num=(q*a) + b
    
    while num > c:
        num-=a
    print(num)