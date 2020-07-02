def parstr(s):
    t, ans = 0, 0
    for i in range(len(s)):
        if s[i] == '<':
            t += 1
        else:
            t -= 1
            if t == 0:
                ans = max(ans, i+1)
            elif t < 0:
                break
    print(ans)


num = int(input())
for _ in range(num):
    s = input()
    parstr(s)
