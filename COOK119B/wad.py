def binary_search(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return False


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = 0
    f = 0
    for i in a:
        if i == m:
            f+=1
            break
    a.sort()
    k = m-1
    while k > 1:
        if (not binary_search(a,0,n-1,k)):
            c = 1
            break
        k -= 1
    if c == 1:
        print(-1)
    else:
        if f == 0:
            print(n)
        else:
            print(n-f)