n=int(input())
for i in range(n):
    s=input()
    rev=''
    for i in s:
        rev=i+rev
    print(int(rev))