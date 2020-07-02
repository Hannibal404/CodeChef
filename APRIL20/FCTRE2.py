def SieveOfEratosthenes(n, prime, primesquare, a):
    for i in range(2, n+1):
        prime[i] = True

    for i in range((n * n + 1)+1):
        primesquare[i] = False

    prime[1] = False

    p = 2
    while(p * p <= n):
        if (prime[p] == True):
            i = p * 2
            while(i <= n):
                prime[i] = False
                i += p
        p += 1

    j = 0
    for p in range(2, n+1):
        if (prime[p] == True):
            a[j] = p

            primesquare[p * p] = True
            j += 1


def countDivisors(n):
    if (n == 1):
        return 1

    prime = [False]*(n + 2)
    primesquare = [False]*(n * n + 2)

    a = [0]*n

    SieveOfEratosthenes(n, prime, primesquare, a)

    ans = 1

    i = 0
    while(1):
        if(a[i] * a[i] * a[i] > n):
            break

        cnt = 1
        while (n % a[i] == 0):
            n = n / a[i]
            cnt = cnt + 1
        ans = ans * cnt
        i += 1

    n = int(n)
    if (prime[n] == True):
        ans = ans * 2

    elif (primesquare[n] == True):
        ans = ans * 3

    elif (n != 1):
        ans = ans * 4

    return ans







class Node():
    def __init__(self, val, cost):
        self.val = val
        self.cost = cost
        self.children = []


def insert(root, a, b, cost):
    if root.val == a:
        root.children.append(Node(b, cost))
        return
    for i in root.children:
        insert(i, a, b, cost)
    return


def depth(root):
    if root == None:
        return 0
    if root.children == []:
        return 1
    else:
        return max([depth(i) for i in root.children])+1








def getPath(root, rarr, x):
    if not root:
        return False

    rarr.append(root)

    if root.val == x:
        return True

    for i in root.children:
        if getPath(i, rarr, x):
            return True

    rarr.pop()
    return False


def prodBetweenNodes(root, n1, n2):
    prod = 1
    path1 = []

    path2 = []
    getPath(root, path1, n1)
    getPath(root, path2, n2)

    i = 0
    intersection = 0
    a = 0
    while(i != len(path1) and i != len(path2)):
        if (path1[i].val == path2[i].val):
            i += 1
        else:
            a = -1
            intersection = i-1
            break
    if a == 0:
        intersection = i-1
    if len(path1) == 1 or len(path2) == 1:
        if len(path1) == 1:
            for i in path2:
                if i != None and i.cost != None:
                    prod *= i.cost
        elif len(path2) == 1:
            for i in path1:
                prod *= i.cost
    elif len(path1) == 0 or len(path2) == 0:
        prod = 1
    else:
        i = intersection
        while i < len(path1):
            prod *= path1[i].cost
            i += 1
        j = intersection+1
        while j < len(path2):
            prod *= path2[j].cost
            j += 1
    return prod


mod = 1000000007

t = int(input())
for _ in range(t):
    n = int(input())
    ct = []

    for _ in range(n-1):
        ct.append(list(map(int, input().split())))

    cl = list(map(int, input().split()))

    root = Node(ct[0][0],cl[0])
    root.children.append(Node(ct[0][1],cl[1]))

    for i in range(1, n-1):
        prev, val = ct[i][0], ct[i][1]
        temp = root
        insert(temp, prev, val, cl[val-1])
    q = int(input())
    mod = 1000000007
    # printLevelOrder(root)
    for _ in range(q):
        u, v = map(int, input().split())
        if u == v:
            prod = cl[u-1]
            print(countDivisors(prod) % mod)
        else:
            prod = prodBetweenNodes(root, u, v)
            print(prod)
            print(countDivisors(prod) % mod)