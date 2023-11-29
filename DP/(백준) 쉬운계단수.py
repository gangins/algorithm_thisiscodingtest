N = int(input())

dp = [[0]*10 for _ in range(N+1)]

# 길이가 1인 계단 수 초기화
for i in range(1, 10):
    dp[1][i] = 1

# 길이가 2 이상인 계단 수 계산
for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)
