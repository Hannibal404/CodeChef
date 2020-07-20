def predecence(operator):
    if operator == '^':
        return 3
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1
    else:
        return 0


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = ""
    i = 0
    op = []
    while i < n:
        if s[i] == "(":
            op.append("(")
        elif s[i].isalpha():
            ans += s[i]
        elif s[i] == ")":
            while op[-1] != "(":
                ans += op.pop()
            op.pop()
        else:
            while len(op) > 0 and predecence(s[i]) <= predecence(op[-1]):
                ans += op.pop()
            op.append(s[i])
        i += 1
    while len(op) > 0:
        ans += op.pop()
    print(ans)
