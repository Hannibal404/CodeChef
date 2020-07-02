dict = {"POUNDS": 0.84,"LIRA":2040, "FRANCS":9.85, "MARKS":3.23, "YEN":260}


t = int(input())
for _ in range(t):
    am, cur = input().split()
    am = int(am)
    fin = am * dict[cur]
    if fin == int(fin):
        print("$"+str(am),"CONVERTS TO",int(fin),cur)
    else:
        print("$"+str(am),"CONVERTS TO",round(fin,2),cur)