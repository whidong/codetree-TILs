def in_range(x, y, n):
    return 0 < x <= n and 0 < y <= n

n, t= map(int, input().split())
r, c, d = map(str, input().split())
r, c = int(r), int(c)
dic = 0
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {'R': 0,'D': 1,'U': 2,'L': 3}
dic = mapper[d]

for i in range(t):
    nx, ny = r + dxs[dic], c + dys[dic]
    if in_range(nx, ny, n):
        r, c = nx, ny
    else:
        dic = 3 - dic

    
print(r, c)