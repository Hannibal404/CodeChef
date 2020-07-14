from collections import defaultdict


def findAns(ac, bc, c, s, small):
    for i in ac.keys():
        if (ac[i] & 1) > 0:
            return -1
    for j in bc.keys():
        if (bc[j] & 1) > 0:
            return -1
    ans = 0
    for k in s:
        r = max(ac[k], bc[k])//2
        # print(k,r)
        if r <= c:
            if (k*r) > (2*small*r):
                ans += (2*small*r)
            else:
                ans += k * r
            c -= r
        else:
            if k*c > 2*c*small:
                ans += 2*c*small
            else:
                ans += k*c
            c = 0
        if c == 0:
            return ans

    return 0


t = int(input())
for _ in range(t):
    n = int(input())
    ac, bc = defaultdict(int), defaultdict(int)
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    i, j, c = 0, 0, 0
    s = set()
    while i < n and j < n:
        if a[i] == b[j]:
            i += 1
            j += 1
        elif a[i] > b[j]:
            ac[b[j]] += 1
            c += 1
            s.add(b[j])
            j += 1
        elif b[j] > a[i]:
            bc[a[i]] += 1
            c += 1
            s.add(a[i])
            i += 1
    while i < n:
        ac[a[i]] += 1
        c += 1
        s.add(a[i])
        i += 1

    while j < n:
        bc[b[j]] += 1
        c += 1
        s.add(b[j])
        j += 1
    # print(ac.keys())
    # print(bc.keys())
    # print(s,c)
    s = list(s)
    s.sort()
    c //= 4
    small = min(a[0], b[0])
    # print(small,"smla")
    print(findAns(ac, bc, c, s, small))


# 1
# 8
# 3 3 3 3 4 4 5 6
# 5 6 8 8 8 8 8 8

    # for i in a:
    #     ac[i] += 1
    # for j in b:
    #     bc[j] += 1
    # difel = []
    # aset, bset = set(a), set(b)
    # unab = aset.union(bset)
    # f = True
    # for i in unab:
    #     if ac[i] == bc[i]:
    #         pass
    #     elif (ac[i] + bc[i]) % 2 != 0:
    #         f = False
    #         break
    #     else:
    #         difel += [i] * abs((ac[i] - bc[i])//2)
    # if not f:
    #     print(-1)
    #     continue
    # # print(sum(difel[:len(difel)//2]))
    # minun = min(unab)


# while (i < n)
#         {
#             lol1[a[i]] += 1;
#             i++;
#             count++;
#             s.insert(a[i]);
#         }
#         while (j < n)
#         {
#             lol2[b[j]] += 1;
#             j++;
#             count++;
#             s.insert(b[j]);
#         }
#         lli ans = 0;
#         //cout << count << " ";
#         count = count / 4;
#         lli smallest = a[0] < b[0] ? a[0] : b[0];

#         ans = find_ans(lol1, lol2, count, s, smallest);
#         cout << ans << endl;
