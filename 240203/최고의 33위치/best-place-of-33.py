n = int(input())
k = []
for i in range(n):
    k.append(list(map(int, input().split())))

def count(m, a, b):
    cnt = 0
    for i in range(a-1,a+2):
        for j in range(b-1, b+2):
            if m[i][j] == 1:
                cnt += 1
    return cnt
max_num =0
for i in range(1, n-1):
    for j in range(1, n-1):
        g = count(k, i, j)
        if max_num <= g:
            max_num = g
print(max_num)