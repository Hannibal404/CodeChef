class Node():
    def __init__(self, val):
        self.val = val
        self.children = []


def insert(root, a, b):
    if root.val == a:
        root.children.append(Node(b))
        return
    for i in root.children:
        insert(i, a, b)


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
        i = intersection+1
        while i < len(path1):
            prod *= path1[i].cost
            i += 1
        j = intersection+1
        while j < len(path2):
            prod *= path2[j].cost
            j += 1
    return prod


a = 1
arr = [2, 3, 4, 5, 6, 7, 8, 9]
root = Node(a)

for i in arr:
    insert(root, i-1, i)
print(depth(root))
