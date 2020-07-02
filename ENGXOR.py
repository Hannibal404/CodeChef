def mXOR(x, y): 
    return ((x | y) & (~x | ~y))

def count1(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 

t=int(input("Test cases = "))
for i in range(t):
    n,q=map(int,input().split())
    al=list(map(int,input().split()))
    for i in range(q):
        ne,no=0,0
        qu=int(input())
        for i in range(n):
            if mXOR(qu,al[i])%2==0:
                ne+=1
            else:
                no+=1
        print(ne,no)