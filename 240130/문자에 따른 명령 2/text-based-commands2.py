dirm = 3
x, y =0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
k = list(input())

for i in k:
    if i == "L":
        dirm = (dirm+4-1)%4 

    elif i == "R":
        dirm = (dirm+1)%4

    elif i == "F":
        x, y = x + dx[dirm], y + dy[dirm]
print(x, y)