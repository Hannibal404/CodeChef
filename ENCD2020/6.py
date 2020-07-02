t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a= list(map(int,input().split()))
    i = 0
    j = i+k - 1
    sum = sum(a[i:j+1])
    msum = sum
    while i < n -1:
        sum -= a[i]
        i += 1
        j += 1
        if j>=n:
            j%=n
        sum += a[j]
        if sum>msum:
            msum = sum
    print(msum)