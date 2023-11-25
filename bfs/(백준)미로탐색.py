# 입력받기
n, m = map(int, input().split())
# 미로
maze = []
# 상하 좌우 이동 범위
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 입력 받기
for i in range(n):
    maze.append(list(map(int, list(input()))))


# bfs를 사용하여 문제를 해결하였다..
def solution(maze):
    # 스텍에 시작점을 추가한다.
    queue = [[0, 0]]
    # 스텍이 빌때까지 반복
    while queue:
        # 스텍에 저장된 값 pop
        x, y = queue.pop(0)
        # 상하좌우로 이동
        for idx in range(4):
            xx = x + dx[idx]
            yy = y + dy[idx]
            # 도착점이라면 결과 출력
            if (xx == n - 1) and (yy == m - 1):
                print(maze[x][y] + 1)
                queue.clear()
                break
            # 이동할 수 있을 경우 이동 횟수 +1 하고 스텍에 해당 좌표를 추가한다.
            if (0 <= xx < n) and (0 <= yy < m):
                if maze[xx][yy] == 1:
                    maze[xx][yy] = (maze[x][y] + 1)
                    queue.append([xx, yy])


solution(maze)