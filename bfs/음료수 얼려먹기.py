from collections import deque

n = int(input())

for t in range(n):
    I = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    arr = [[-1] * I for _ in range(I)]  # 방문하지 않은 셀을 나타내기 위해 -1로 초기화

    dx = [2, 2, 1, 1, -1, -1, -2, -2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        arr[x][y] = 0  # 시작점의 거리는 0

        while queue:
            x, y = queue.popleft()
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < I and 0 <= ny < I and arr[nx][ny] == -1:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx, ny))
                    if nx == ex and ny == ey:
                        return arr[nx][ny]
        return 0
    print(bfs(sx, sy))
