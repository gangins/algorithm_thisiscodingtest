from collections import deque

n = int(input())
arr = [list(input().split()) for _ in range(n)]
arr_br =[['']*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr_br[i][j]= 'G'
        else:
            arr_br[i][j]= arr[i][j]

dx = [1,-1,0,0]
dx = [0,0,1,-1]
def dfs(i,j):
    x,y = i,j

    while q:
        q.popleft()



#  색맹인사람
for i in range(n):
    for j in range(n):
        if arr[i][j]

            dfs(i,j)