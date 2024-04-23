n, t = map(int, input().split())
k = list(input())
box = []
for i in range(n):
    box.append(list(input().split()))
x, y = n//2, n//2
dx, dy = [-1, 0, 1, 0], [0,-1, 0, 1]
now, result = 0, 0
result += int(box[x][y])
for j in k:
    if j == "L":
        now = (now+1)%4
    elif j == "R":
        now = (now+3)%4
    elif j == "F":
        nx = x + dx[now]
        ny = y + dy[now]
        if nx >= 0 and nx < n and ny >= 0 and ny <n:
            x = nx
            y = ny
            result += int(box[x][y])
        else:
            pass
print(result)