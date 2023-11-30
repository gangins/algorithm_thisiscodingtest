from collections import deque

n, m = map(int,input().split())

Q =deque()
arr = []

for i in range(m):
    lst= list(map(int,input().split()))
    arr.append(lst)
    for j in range(n):
        if lst[j] ==1:
            Q.append((i,j,0))

dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bfs():
    max_day = 0
    while Q:
        x, y, day = Q.popleft()
        max_day = max(max_day, day)
        for i in range(4):
            nx = x + dx[i]
            ny= y +dy[i]
            if 0<= nx < m and 0<= ny < n:
                if arr[nx][ny] == 0:
                    arr[nx][ny] =1
                    Q.append((nx, ny, day+1))
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                return -1
            
    return max_day
result = bfs(0)

print(result)