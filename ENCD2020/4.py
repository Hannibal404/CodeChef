t = int(input())
for _ in range(t):
    n, = map(int,input().split())
    a= list(map(int,input().split()))
    a.sort()
    dic = {}
    for i in range(n):
        if a[i] in dic.keys():
            dic[a[i]]+=1
        else:
            dic[a[i]] = 1
    for i in dic.keys():
        print(str(i)+":"+str(dic[i]))