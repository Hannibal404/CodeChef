mod = 998244353


def ngcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a//b, b, a % b
        x0, x1 = x1, x0-q*x1
        y0, y1 = y1, y0-q*y1
    return a, x0, y0


def modInverse(a, m):
    g, x, y = ngcd(a, m)
    if g != 1:
        raise Exception
    else:
        return x % m


nil = 0
one = 1

t = int(input())
for _ in range(t):
    l = input()
    qcount = l.count("#")
    if qcount == 1:
        print(modInverse(4, mod), modInverse(4, mod),
              modInverse(4, mod), modInverse(4, mod))
    else:

        for i in range(len(l)):
            if l[i] == "(":
                b += 1
            elif l[i] == ")":
                b -= 1



# # cook your dish here
# import sys
# input = sys.stdin.readline


# def prob(l,r,s):
#     if r==l:
#         count = [1,1,1,1]
#         return count
#     else:
#         ind = opretor(l, r, s)
#         opr = s[ind]
#         count_l = prob(l+1, ind-1, s)
#         count_r = prob(ind+1, r-1, s)
#         cont_t = [0,0,0,0]

#         if opr == '&':
#             cont_t[1] = (count_l[1]*count_r[1])
#             cont_t[0] = (count_l[0]*sum(count_r)+ count_l[2]*count_r[3] + (sum(count_l[1:4]) * count_r[0])  + count_l[3]*count_r[2])
#             cont_t[2] = (count_l[2]*count_r[1]+ count_l[2]*count_r[2] + count_l[1]*count_r[2] )
#             cont_t[3] = (count_l[3]*count_r[1]  + count_l[3]*count_r[3]+ count_l[1]*count_r[3])
#             return cont_t

#         elif opr == '^':
#             cont_t[0] = count_l[1]*count_r[1]  + count_l[3]*count_r[3] + count_l[0]*count_r[0]+ count_l[2]*count_r[2]
#             cont_t[1] = count_l[1]*count_r[0]  + count_l[2]*count_r[3] + count_l[3]*count_r[2]+ count_l[0]*count_r[1]
#             cont_t[2] = count_l[1]*count_r[3]  + count_l[2]*count_r[0] + count_l[0]*count_r[2]+ count_l[3]*count_r[1]
#             cont_t[3] = count_l[1]*count_r[2]  + count_l[0]*count_r[3] + count_l[3]*count_r[0]+ count_l[2]*count_r[1]
#             return cont_t

#         elif opr == '|':
#             cont_t[0] = count_l[0] * count_r[0]
#             cont_t[1] = count_l[1] * sum(count_r) + (count_l[0]+count_l[2]+count_l[3])*count_r[1] + count_l[2]*count_r[3] + count_l[3]*count_r[2]
#             cont_t[2] = count_l[2]*count_r[0]  + count_l[2]*count_r[2]+ count_l[0]*count_r[2]
#             cont_t[3] = count_l[3]*count_r[0]  + count_l[3]*count_r[3]+ count_l[0]*count_r[3]
#             return cont_t

# def opretor(l,r,s):
#     cl = 0
#     cr = 0
#     for i in range(l,r+1):
#         if s[i] == '(':
#             cl +=1
#         elif s[i] == ')':
#             cr += 1
#         if (s[i] == '&' or s[i] == '|' or s[i] == '^') and cl == cr+1:
#             return i

            
# def Inverse(a, m) : 
#     m0 = m 
#     y = 0
#     x = 1
  
#     if (m == 1) : 
#         return 0
  
#     while (a > 1) : 

#         q = a // m 
  
#         t = m 
  
#         m = a % m 
#         a = t 
#         t = y 
  
#         y = x - q * y 
#         x = t 
  
#     if (x < 0) : 
#         x = x + m0 
  
#     return x 


# mod = 998244353

# for t in range(int(input())):
#     s = input()

#     array = prob(0, len(s)-2, s)

#     summation= sum(array)

#     modulus = Inverse(summation, mod)

#     for i in range(4):
#         if i!= 3:
#             print(array[i]*modulus%mod, end=' ')
#         else:
#             print(array[i]*modulus%mod)
