t=int(input())
for i in range(t):
    lapin=True
    fm=[0 for i in range(26)]
    sm=[0 for i in range(26)]
    st=input()
    n=len(st)
    fh=st[:n//2]
    if n%2==0:
        sh=st[n//2:]
    else:
        sh=st[n//2+1:]
    for i in fh:
        fm[ord(i)-97]+=1
    for i in sh:
        sm[ord(i)-97]+=1
    for i in range(26):
        if fm[i]!=sm[i]:
            lapin=False
    if lapin==True:
        print("YES")
    else:
        print("NO")