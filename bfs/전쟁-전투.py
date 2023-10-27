from collections import deque

N,M = map(int,input().split())
arr = [list(input()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
    Q = deque()
    Q.append((x,y))
    visited[x][y] = 1
    cnt = 1
    color = arr[x][y]
    while Q :
        X,Y = Q.popleft()

        for i in range(4):
            nx = X + dx[i]
            ny = Y + dy[i]

            if 0<= nx < N and 0<= ny <M and not visited[nx][ny] and arr[nx][ny] == color:
                Q.append((nx,ny))
                visited[ nx ][ny] =1
                cnt +=1

    return cnt * cnt


ansW = 0
ansB =0
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            power = bfs(i, j)
            if arr[i][j] == 'W':
                ansW += power

            else:
                ansB += power
print(ansW, ansB)