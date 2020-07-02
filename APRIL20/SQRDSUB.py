t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    pow2l = []
    for i in range(n):
        y = s[i]
        if y % 2 != 0:
            pow2l.append(0)
        elif y % 4 == 0:
            pow2l.append(2)
        else:
            pow2l.append(1)
    nosub = 0
    i = 0
    while i < n:
        j = i+1
        if pow2l[i] > 1:
            nosub += n-i
            i = j
        elif pow2l[i] == 1:
            a = 0
            j = i+1
            while j < n:
                if pow2l[j] > 0:
                    nosub += (n-j)
                    a = -1
                    break
                else:
                    j += 1
            i += 1
        else:
            if i == n-1:
                nosub += 1
                break
            nzero = 1
            while j < n:
                a = 0
                if pow2l[j] == 0:
                    nzero += 1
                    if j == n-1:
                        nosub += (nzero*(nzero+1))//2
                        i = j+1
                        break
                    j += 1
                elif pow2l[j] > 1:
                    nosub += (((n-i)*((n-i)+1))//2) - (((n-j)*((n-j)-1))//2)
                    break
                else:
                    nosub += (nzero*(nzero+1))//2
                    k = j+1
                    while k < n:
                        if pow2l[k] > 0:
                            nosub += (nzero+1)*(n-k)
                            a = -1
                            break
                        else:
                            k += 1
                    if a == -1 or k >= n:
                        break
            i = j+1
    print(nosub)
