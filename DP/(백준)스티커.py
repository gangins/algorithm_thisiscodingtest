T = int(input())
for i in range(T):
    M = int(input())
    dp = [list(map(int,input().split())) for _ in range(2)]

    dp[1][1] += dp[0][0]
    dp[0][1] += dp[1][0]

    for i in range(2,M):
        dp[0][i] += max(dp[1][i-1],dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])


    print(max(dp[0][M-1],dp[1][M-1]))