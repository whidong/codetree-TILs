n, m = map(int, input().split())
k = []
for i in range(n):
    k.append(list(map(int, input().split())))
result = 0
for i in range(n):
    r_cnt = 0
    l_cnt = 0
    r_p =0
    l_p = 0
    r_b = False
    l_b = False
    for j in range(n):
        if k[i][j] == r_p:
            r_cnt += 1
            if m <= r_cnt + 1:
                r_b = True
        else:
            r_cnt = 0
        if k[j][i] == l_p:
            l_cnt += 1
            if m <= l_cnt + 1:
                l_b = True
        else:
            l_cnt = 0
        r_p = k[i][j]
        l_p = k[j][i]
    if r_b == True:
        result += 1
    if l_b == True:
        result += 1
print(result)