n=int(input())
bud=[]
for i in range(n):
    bud.append(int(input()))
bud.sort()
mrev=0
for i in range(n):
    x=bud[i]*(n-i)
    if x>mrev:
        mrev=x
print(mrev)