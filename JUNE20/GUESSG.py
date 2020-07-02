def bs(l, u):
    return l + (u-l)//2


n = int(input())
if n == 1:
    print(1)
    quit()
x = n // 2
print(x)
y = input()

if y == 'E':
    quit()

x1 = n // 2
print(x1)
y1 = input()

l, u = 1, n
l1, u1 = 1, n

while True:
    if y == 'L':
        u = x-1
        x = (l+u)//2
        if x < 1:
            x = 1
        if x > n:
            x = n
        print(x)
        y = input()
        if y == 'E':
            quit()
    else:
        l = x+1
        x = (l+u)//2
        if x < 1:
            x = 1
        if x > n:
            x = n
        print(x)
        y = input()
        if y == 'E':
            quit()
    if y1 == 'L':
        u1 = x1-1
        x1 = (l1+u1)//2
        if x1 < 1:
            x1 = 1
        if x1 > n:
            x1 = n
        print(x1)
        y1 = input()
        if y1 == 'E':
            quit()
    else:
        l1 = x1+1
        x1 = (l1+u1)//2
        if x1 < 1:
            x1 = 1
        if x1 > n:
            x1 = n
        print(x1)
        y1 = input()
        if y1 == 'E':
            quit()
