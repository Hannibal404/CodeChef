n = int(input())

print(1)
out = input()
if out == 'E':
    quit()
else:
    l, u = 1, n
    while True:
        if out == 'L':
            x = (l+u)//2
            print(x)
            out = input()
            if out == 'E':
                quit()
            elif out == 'G':
                l = x + 1
                x = (l + u)//2
            else:
                u = x - 1
                x = (l + u)//2
            if l == u:
                print(l)
                out = input()
                if out == 'E':
                    quit()
            else:
                print(l)
                out = input()
                if out == 'E':
                    quit()
        else:
            l += 1
            print(l)
            out = input()
            if out == 'E':
                quit()
