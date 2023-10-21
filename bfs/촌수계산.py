T = int(input())
S, E = map(int, input().split())
n = int(input())

arr = [[] for _ in range(T + 1)]

for _ in range(n):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

visited = [False] * (T + 1)

def dfs(S, cnt):
    if S == E:
        result.append(cnt)
        return

    visited[S] = True

    for i in arr[S]:
        if not visited[i]:
            dfs(i, cnt + 1)

result = []
dfs(S, 0)

if result:
    print(result[0])
else:
    print(-1)
