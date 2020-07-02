t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    trav = 0
    flo = 0
    for _  in range(q):
        i, f = map(int,input().split())
        trav += abs(i - flo) + abs(f - i)
        flo = f
    print(trav) 