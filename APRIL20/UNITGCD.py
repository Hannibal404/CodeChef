# t = int(input())
# for i in range(t):
#     n = int(input())
#     if n == 1:
#         print(1)
#         print(1, 1)
#     elif n == 2:
#         print(1)
#         print(2, 1, 2)
#     elif n == 3:
#         print(1)
#         print(3, 1, 2, 3)
#     else:
#         print(n//2)
#         print(3, 1, 2, 3)
#         for i in range(3, n+1, 2):
#             x = i+1
#             if x <= n:
#                 if x != n:
#                     print(2, x, x+1)
#                 else:
#                     print(2, 1, x)

t=int(input())
for _ in range(t):
    n=int(input())
    if n==1:
        print(1)
        print(1,1)
    else:
        print(n//2)
        for i in range(n//2):
            if n%2==1 and i==0:
                pre = "3 "
            else:
                pre = "2 "
            out= pre+str((i*2)+1) + " " + str((i+1)*2)
            if n%2==1:
                if i==0:
                    out+= " " + str(n)
            print(out)