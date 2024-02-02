def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

n, t= map(int, input().split())
r, c, d = map(str, input().split())
r, c = int(r)-1, int(c)-1
dic = 0
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
if d == "U":
    dic = 1
elif d == "D":
    dic = 2
elif d == "R":
    dic = 0
elif d == "L":
    dic = 3
for i in range(t):
    nx, ny = r + dxs[dic], c + dys[dic]
    if in_range(nx, ny, n):
        r, c = nx, ny
    else:
        dic = 3 - dic

    
print(r+1, c+1)