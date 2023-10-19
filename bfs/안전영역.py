from collections import deque

n = int(input())
maxheight = 0
arr = []
for i in range(n):
    lst = list(map(int, input().split()))
    arr.append(lst)
    if maxheight < max(lst):
        maxheight = max(lst)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, m):
    Q = deque()
    Q.append((x, y))
    visited[x][y] = 1
    while Q:
        X, Y = Q.popleft()
        for i in range(4):
            nx = X + dx[i]
            ny = Y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] <= m and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    Q.append((nx, ny))

maxcnt = 0
for m in range(maxheight):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > m and visited[i][j] == 0:
                bfs(i, j, m)
                cnt += 1
    if maxcnt < cnt:
        maxcnt = cnt

print(maxcnt)
