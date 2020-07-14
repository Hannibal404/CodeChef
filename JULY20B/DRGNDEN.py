def fun1(a, b, nt):
    a[b-1] = nt


def fun2(b, c, a, h):
    if b == c:
        return a[b-1]
    elif b < c:
        if max(h[b-1:c]) > h[b-1]:
            return -1

    else:
        if max(h[c-1:b]) > h[c-1]:
            return -1

    return


n, q = map(int, input().split())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

for _ in range(q):
    x, b, y = map(int, input())
    if x == 1:
        fun1(a, b, y)
    else:
        print(fun2(b, y, a, h))
