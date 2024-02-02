n = int(input())

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
k =[]
for i in range(n):
    k.append(list(map(int, input().split())))

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n


result = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for x, y in zip(dx, dy):    
            nx, ny = x + i, y + j
            if in_range(nx, ny, n) and k[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            result += 1

print(result)