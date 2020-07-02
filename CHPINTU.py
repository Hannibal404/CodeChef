t=int(input("Enter no. of testcases>>"))
for i in range(t):
	n,m=map(int,input().split())
	fr=list(map(int,input().split()))
	fc=list(map(int,input().split()))
	cl=[0 for i in range(m+1)]
	for i in range(n):
		cl[fr[i]]+=fc[i]
	cl.sort()
	for i in cl:
		if i>0:
			print(i)
			break