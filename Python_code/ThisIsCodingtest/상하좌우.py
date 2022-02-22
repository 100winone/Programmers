dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x, y = 1, 1
dir_char  = ['L', 'R', 'U', 'D']
n = int(input())
arr = input().split()
for dir in arr:
    for idx in range(4):
        if dir_char[idx] == dir:
            nx = x + dx[idx]
            ny = y + dy[idx]
            break
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)