from collections import deque

n,m = map(int,input().split())
arr =[]
queue = deque()
visited = [[0]* m for _ in range(m)]
for i in range(N):
    row = list(map(int, input().split()))

    # 목표지점 찾기
    for j in range(M):
        if row[j] == 2:
            queue.append((i, j))
            visited[i][j] = True
            row[j] = 0
    arr.append(row)



for i in range():
