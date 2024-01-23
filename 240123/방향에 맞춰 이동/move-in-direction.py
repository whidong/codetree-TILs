n = int(input())

x, y = 0, 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for i in range(0, n):
    d, k = input().split()
    k = int(k)
    if d == "E":
        x += k*dx[0]
        y += k*dy[0]
    elif d == "S":
        x += k*dx[1]
        y += k*dy[1]
    elif d == "W":
        x += k*dx[2]
        y += k*dy[2]
    elif d == "N":
        x += k*dx[3]
        y += k*dy[3]


print(x, y)