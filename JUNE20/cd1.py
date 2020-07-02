try:
	def min_ops(a,b):
		if a==b:
			return 0
		if b==[0]*3:
			return 1
		if a==[0]*3:
			if b==[b[0]]*3:
				return 1
			if b==[0,b[1],b[1]]:
				return 1
			if b==[b[0],0,b[0]]:
				return 1
			if b==[b[0],b[0],0]:
				return 1
			if b.count(0)==2:
				return 1
			if b.count(0)==1:
				return 2
			if b.count(0)==0:
				if b[0]==b[1] and b[0]!=b[2]:
					return 2
				if b[0]==b[2] and b[0]!=b[1]:
					return 2
				if b[1]==b[2] and b[0]!=b[1]:
					return 2
				else:
					return 3
		if a.count(0)==2:
			if a[0]==a[1]:
				if b[0]==b[1]:
					if b[0]==b[2]-a[2]:
						return 1
					else:
						return 2
				else:
					if b[0]==b[2]-a[2]:
						return 2
					if b[1]==b[2]-a[2]:
						return 2
					else:
						return 3
			if a[2]==a[1]:
				if b[2]==b[1]:
					if b[2]==b[0]-a[0]:
						return 1
					else:
						return 2
				else:
					if b[2]==b[0]-a[0]:
						return 2
					if b[1]==b[0]-a[0]:
						return 2
					else:
						return 3
			if a[0]==a[2]:
				if b[0]==b[2]:
					if b[0]==b[1]-a[1]:
						return 1
					else:
						return 2
				else:
					if b[0]==b[1]-a[1]:
						return 2
					if b[2]==b[1]-a[1]:
						return 2
					else:
						return 3
		if a.count(0)==1:
			if a[0]==0:
				if b[0]==b[1]-a[1] and b[0]==b[2]-a[2]:
					return 1
				if (b[1]-b[0])/a[1]==int((b[1]-b[0])/a[1]) and (b[1]-b[0])/a[1]==(b[2]-b[0])/a[2]:
					return 2
				if b[0]==b[2]-a[2] and (b[1]-b[0])/a[1]==int((b[1]-b[0])/a[1]):
					return 2
				if b[0]==b[1]-a[1] and (b[2]-b[0])/a[2]==int((b[2]-b[0])/a[2]):
					return 2
				else:
					return 3
			if a[1]==0:
				if b[1]==b[0]-a[0] and b[1]==b[2]-a[2]:
					return 1
				if (b[0]-b[1])/a[0]==int((b[0]-b[1])/a[0]) and (b[0]-b[1])/a[0]==(b[2]-b[1])/a[2]:
					return 2
				if b[1]==b[2]-a[2] and (b[0]-b[1])/a[0]==int((b[0]-b[1])/a[0]):
					return 2
				if b[1]==b[0]-a[0] and (b[2]-b[1])/a[2]==int((b[2]-b[1])/a[2]):
					return 2
				else:
					return 3
			if a[2]==0:
				if b[2]==b[1]-a[1] and b[2]==b[0]-a[0]:
					return 1
				if (b[1]-b[2])/a[1]==int((b[1]-b[2])/a[1]) and (b[1]-b[2])/a[1]==(b[0]-b[2])/a[0]:
					return 2
				if b[2]==b[0]-a[0] and (b[1]-b[2])/a[1]==int((b[1]-b[2])/a[1]):
					return 2
				if b[2]==b[1]-a[1] and (b[0]-b[2])/a[0]==int((b[0]-b[2])/a[0]):
					return 2
				else:
					return 3
		if a.count(0)==0:
			if b[0]-a[0]==b[1]-a[1] and b[0]-a[0]==b[2]-a[2]:
				return 1
			if b[0]-a[0]==b[1]-a[1] and b[2]==a[2]:
				return 1
			if b[1]-a[1]==b[2]-a[2] and a[0]==b[0]:
				return 1
			if b[0]-a[0]==b[2]-a[2] and a[1]==b[1]:
				return 1
			q=[]
			for i in range(3):
				q.append(b[i]/a[i])
			if q==[q[0]]*3 and q[0]==int(q[0]):
				return 1
			if q==[q[0],q[0],1] and q[0]==int(q[0]):
				return 1
			if q==[q[0],1,q[0]] and q[0]==int(q[0]):
				return 1
			if q==[1,q[1],q[1]] and q[1]==int(q[1]):
				return 1
			if q==[0]*3:
				return 1
			if q.count(1)==2:
				return 1
			if b==[b[0]]*3:
				return 2
			if b==[0,b[1],b[1]]:
				return 2
			if b==[b[0],0,b[0]]:
				return 2
			if b==[b[0],b[0],0]:
				return 2
			d=[]
			for i in range(3):
				d.append(b[i]-a[i])
			if d[0]==d[1]:
				return 2
			if d[1]==d[2]:
				return 2
			if d[0]==d[2]:
				return 2
			if b[0]/a[0]==int(b[0]/a[0]):
				k=int(b[0]/a[0])
				w1=b[1]-k*a[1]
				w2=b[2]-k*a[2]
				if w1==w2:
					return 2
				if w1==b[2]-a[2]:
					return 2
				if w2==b[1]-a[1]:
					return 2
				if w1==0 or w2==0:
					return 2
			if b[1]/a[1]==int(b[1]/a[1]):
				k=int(b[1]/a[1])
				w1=b[0]-k*a[0]
				w2=b[2]-k*a[2]
				if w1==w2:
					return 2
				if w1==b[2]-a[2]:
					return 2
				if w2==b[0]-a[0]:
					return 2
				if w1==0 or w2==0:
					return 2
			if b[2]/a[2]==int(b[2]/a[2]):
				k=int(b[2]/a[2])
				w1=b[1]-k*a[1]
				w2=b[0]-k*a[0]
				if w1==w2:
					return 2
				if w1==b[0]-a[0]:
					return 2
				if w2==b[1]-a[1]:
					return 2
				if w1==0 or w2==0:
					return 2
			if a[1]==a[2] and a[1]==a[0]:
				return 3
			if a[1]==a[2]:
				if (b[1]-b[0])/(a[1]-a[0])==int((b[1]-b[0])/(a[1]-a[0])):
					w=int((a[1]*b[0]-a[0]*b[1])/(a[1]-a[0]))
					k=int((b[1]-b[0])/(a[1]-a[0]))
					if a[2]+w==b[2]:
						return 2
					if a[2]*k+w==b[2]:
						return 2
					if a[2]==b[2]:
						return 2
				if (b[0]-b[2])/(a[0]-a[2])==int((b[0]-b[2])/(a[0]-a[2])):
					w=int((a[0]*b[2]-a[2]*b[0])/(a[0]-a[2]))
					k=int((b[0]-b[2])/(a[0]-a[2]))
					if a[1]+w==b[1]:
						return 2
					if a[1]*k+w==b[1]:
						return 2
					if a[1]==b[1]:
						return 2
			if a[0]==a[1]:
				if (b[1]-b[2])/(a[1]-a[2])==int((b[1]-b[2])/(a[1]-a[2])):
					w=int((a[1]*b[2]-a[2]*b[1])/(a[1]-a[2]))
					k=int((b[1]-b[2])/(a[1]-a[2]))
					if a[0]+w==b[0]:
						return 2
					if a[0]*k+w==b[0]:
						return 2
					if a[0]==b[0]:
						return 2
				if (b[0]-b[2])/(a[0]-a[2])==int((b[0]-b[2])/(a[0]-a[2])):
					w=int((a[0]*b[2]-a[2]*b[0])/(a[0]-a[2]))
					k=int((b[0]-b[2])/(a[0]-a[2]))
					if a[1]+w==b[1]:
						return 2
					if a[1]*k+w==b[1]:
						return 2
					if a[1]==b[1]:
						return 2
			if a[0]==a[2]:
				if (b[1]-b[2])/(a[1]-a[2])==int((b[1]-b[2])/(a[1]-a[2])):
					w=int((a[1]*b[2]-a[2]*b[1])/(a[1]-a[2]))
					k=int((b[1]-b[2])/(a[1]-a[2]))
					if a[0]+w==b[0]:
						return 2
					if a[0]*k+w==b[0]:
						return 2
					if a[0]==b[0]:
						return 2
				if (b[1]-b[0])/(a[1]-a[0])==int((b[1]-b[0])/(a[1]-a[0])):
					w=int((a[1]*b[0]-a[0]*b[1])/(a[1]-a[0]))
					k=int((b[1]-b[0])/(a[1]-a[0]))
					if a[2]+w==b[2]:
						return 2
					if a[2]*k+w==b[2]:
						return 2
					if a[2]==b[2]:
						return 2

			if (b[1]-b[2])/(a[1]-a[2])==int((b[1]-b[2])/(a[1]-a[2])):
				w=int((a[1]*b[2]-a[2]*b[1])/(a[1]-a[2]))
				k=int((b[1]-b[2])/(a[1]-a[2]))
				if a[0]+w==b[0]:
					return 2
				if a[0]*k+w==b[0]:
					return 2
				if a[0]==b[0]:
					return 2
			if (b[1]-b[0])/(a[1]-a[0])==int((b[1]-b[0])/(a[1]-a[0])):
				w=int((a[1]*b[0]-a[0]*b[1])/(a[1]-a[0]))
				k=int((b[1]-b[0])/(a[1]-a[0]))
				if a[2]+w==b[2]:
					return 2
				if a[2]*k+w==b[2]:
					return 2
				if a[2]==b[2]:
					return 2
			if (b[0]-b[2])/(a[0]-a[2])==int((b[0]-b[2])/(a[0]-a[2])):
				w=int((a[0]*b[2]-a[2]*b[0])/(a[0]-a[2]))
				k=int((b[0]-b[2])/(a[0]-a[2]))
				if a[1]+w==b[1]:
					return 2
				if a[1]*k+w==b[1]:
					return 2
				if a[1]==b[1]:
					return 2
			else:
				return 3
	t=int(input())
	for i in range(t):
		a=list(map(int,input().split()))
		b=list(map(int,input().split()))
		print(min_ops(a,b))
except EOFError as e: pass