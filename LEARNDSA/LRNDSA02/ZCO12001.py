n = int(input())
b = list(map(int, input().split()))
mdep = 0
mdeps = 0
dep = 0
lini = 0
ll = 0
ini = 0

for i in range(n):
    if b[i] == 1:
        dep += 1
    else:
        dep -= 1
    if dep > mdep:
        mdep = dep
        mdeps = i + 1
    if dep == 0:
        tll = i - ini + 1
        if tll > ll:
            ll = tll
            lini = ini + 1
        ini = i+1
print(mdep, mdeps, ll, lini)
