mod = 1000000007

def power(x, y, p) : 
    res = 1
    x = x % p  
      
    if (x == 0) : 
        return 0
  
    while (y > 0) : 
        if ((y & 1) == 1) : 
            res = (res * x) % p 

        y = y >> 1
        x = (x * x) % p 
          
    return res 

t = int(input())
for _ in range(t):
    n, a = map(int,input().split())
    el = a
    sum = 0
    p1=1
    for i in range(1,n+1):
        p2 = power(el,(2*i)-1,mod)
        sum += p2%mod
        el*=p2%mod
        el%=mod
        p1 = p2
        sum%=mod
    sum%=mod
    print(sum)