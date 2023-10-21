from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j, cnt):
    q = deque()
    q.append((i, j))
    visited[i][j] = cnt
    house_count = 0  # 각 단지 내 집의 수를 계산하는 변수 추가
    while q:
        x, y = q.popleft()
        house_count += 1  # 각 집 방문 시 집의 수를 증가
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and arr[nx][ny] != 0:
                    q.append((nx, ny))
                    visited[nx][ny] = cnt
    return house_count

lst = []

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and arr[i][j] != 0:
            cnt = 1
            house_count = dfs(i, j, cnt)  # 각 단지 내 집의 수를 계산
            lst.append(house_count)

print(len(lst))  # 총 단지 수 출력
lst.sort()  # 각 단지 내 집의 수를 오름차순 정렬
for count in lst:
    print(count)  # 각 단지 내 집의 수 출력
