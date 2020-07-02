def query(n):
    print(n)
    x = input()
    if x == 'E':
        quit()
    return x


def dodo(l, u):
    m = (l+u)//2
    for i in range(8):
        c = query(1)
        if c == 'L':
            c = query(m)
            if c == 'G':
                dodo(m+1, u)
            else:
                dodo(l, m-1)
            return
    c = query(m)
    if c == 'G':
        dodo(m+1, u)
    else:
        query(m-1)
    return


def search(l, u):
    if u < l:
        return
    elif u == l:
        query(l)
        return
    t1 = l + ((u-l)//3)
    t2 = u - ((u-l)//3)
    c1 = query(t1)
    c2 = query(t2)
    if c1 == 'L' and c2 == 'L':
        search(l, t2-1)
        return
    elif c1 == 'G' and c2 == 'G':
        search(t1+1, u)
        return
    elif c1 == 'L' and c2 == 'G':
        search(l, t1-1)
        search(t2+1, u)
        return
    c1 = query(t2)
    if c1 == 'L':
        search(l, t2-1)
        return
    c2 = query(t1)
    if c2 == 'G':
        search(t1+1, u)
        return
    search(l, t1-1)
    search(t2+1, u)


n = int(input())
m = (1+n)//2
for i in range(8):
    c = query(1)
    if c == 'L':
        c = query(m)
        if c == 'G':
            dodo(m+1, n)
        else:
            dodo(2, m-1)

search(1, n)
