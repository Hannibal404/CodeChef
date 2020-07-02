dic = {"fert": 5000, "lime": 2000, "seed": 1000}


def printstuff(x):
    fer = x/dic["fert"]
    lim = x/dic["lime"]
    sed = x/dic["seed"]
    if fer == int(fer):
        print(int(fer), "BAG(S) FERTILIZER")
    else:
        print(int(fer)+1, "BAG(S) FERTILIZER")
    if lim == int(lim):
        print(int(lim), "BAG(S) LIME")
    else:
        print(int(lim)+1, "BAG(S) LIME")
    if sed == int(sed):
        print(int(sed), "BAG(S) SEED")
    else:
        print(int(sed)+1, "BAG(S) SEED")


a = list(map(int, input().split()))
for i in range(1, a[0]+1):
    printstuff(a[i])
