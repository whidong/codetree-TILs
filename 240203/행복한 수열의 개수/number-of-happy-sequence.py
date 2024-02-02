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
    for j in range(n):
        if k[i][j] == r_p:
            r_cnt += 1
        else:
            r_cnt = 0
        if k[j][i] == l_p:
            l_cnt += 1
        else:
            l_cnt = 0
        r_p = k[i][j]
        l_p = k[j][i]
    if m <= r_cnt + 1:
        result += 1
    if m <= l_cnt + 1:
        result += 1
print(result)