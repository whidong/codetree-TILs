n, t = map(int, input().split())
k = list(input())
box = []
for i in range(n):
    box.append(list(input().split()))
x, y = n//2, n//2
dx, dy = [-1, 0, 1, 0], [0,-1, 0, 1]
now = 0
result = 0
result += int(box[x][y])
for j in k:
    if j == "L":
        now += 1
    elif j == "R":
        now -= 1
    elif j == "F":
        if x + dx[now] == n or x + dx[now] < -1 or y + dy[now] == n or y + dy[now] < -1:
            pass
        else:
            x = x + dx[now]
            y = y + dy[now]
            result += int(box[x][y])
print(result)