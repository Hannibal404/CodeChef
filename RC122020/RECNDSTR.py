t = int(input())
for _ in range(t):
    s = input()
    if s[1:]+s[0] == s[-1] + s[:len(s)-1]:
        print("YES")
    else:
        print("NO")