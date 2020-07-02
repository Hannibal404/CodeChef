t = int(input())
for _ in range(t):
    s = input()
    i = 0
    p = 0
    n = len(s)
    while i < n-1:
        if (s[i] == 'x' and s[i+1] == 'y') or (s[i] == 'y'and s[i+1] == 'x'):
            p += 1
            i += 2
        else:
            i += 1
    print(p)
