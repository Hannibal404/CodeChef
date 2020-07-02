# t=int(input())
# for i in range(t):
#     n,k=map(int,input().split())
#     fl=list(map(int,input().split()))
#     ml=0
#     i=0
#     while i<n:
#         j=i
#         l=0
#         s=set()
#         while j<n:
#             if len(s)<k-1:
#                 s.add(fl[j])
#                 l+=1
#                 j+=1
#             elif len(s)==k-1:
#                 if fl[j] not in s:
#                     break
#                 else:
#                     l+=1
#                     j+=1
#         if l>ml:
#             ml=l
#         if ml==n:
#             break
#         x=i
#         while x<n:
#             if fl[x]==fl[i]:
#                 x+=1
#             else:
#                 break
#         i=x
#         if n-i<ml:
#             break
#     print(ml)

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    f=list(map(int,input().split()))
    ml=0
    i = 0
    j = 0
    l = 0
    flavs = [0 for _ in range(k+1)]
    while i < n - ml:
        while j < n:
            if flavs[f[j]] > 0:
                l+=1
                flavs[f[j]]+=1
                if l > ml:
                    ml = l
                j += 1
            else:
                if (flavs.count(0))> 2:
                    l += 1
                    if l >ml:
                        ml = l
                    flavs[f[j]] +=1
                    j += 1                  
                else:
                    flavs[f[i]] -= 1
                    l -= 1
                    i += 1
    print(ml)