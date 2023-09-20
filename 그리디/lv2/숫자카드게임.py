N, M = map(int, input().split())
result = 0

for i in range(N):
    data = list(map(int, input().split()))

    minval = min(data)

    result = max(result, minval)

print(result)