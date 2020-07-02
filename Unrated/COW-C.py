t = int(input())
sum = 0
for _ in range(t):
    n, m = map(int, input().split())
    sum += m-n+1
print(sum%1000000007)
