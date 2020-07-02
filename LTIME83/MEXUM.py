mod = 998244353


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if min(a) > 1:
        print((2**n) % mod)
    else:
        i = 0
        while i < n:
            if a[i] == 1:
                i += 1
            else:
                break
        c1 = i
        if c1 == n:
            print(((2**(n+1))-1) % mod)
        else:
            sum = ((2**(n-i)) - 1) + (a[i-1]+1)*((2**i)-1)
            csub = (2**i)-1
            j = i
            if j < n:
                num = a[j]
                cj = 0
            while j < n:
                if abs(a[j]-a[i-1]) > 1:
                    sum += (((csub*((cj**2)-1))+1)*(((2**(n-j))-1)*(a[i-1]+1))) % mod
                    break
                else:
                    if num == a[j] and j != n-1:
                        cj += 1
                        j += 1
                    else:
                        if j == n-1 and num == a[j]:
                            cj += 1
                            i = j
                            csub *= ((2**cj)-1) % mod
                            sum += (a[i]+1) * csub
                            j += 1
                        elif j == n-1 and num != a[j]:
                            sum += (a[j]+1) * csub *((2**cj)-1)
                            j += 1
                        else:
                            i = j
                            num = a[j]
                            csub *= ((2**cj)-1) % mod
                            sum += (a[i]+1) * csub
                            j += 1
                            cj = 0
            print((sum+1) % mod)
