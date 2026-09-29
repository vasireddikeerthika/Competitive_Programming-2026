n, m = map(int, input().split())

grid = []

for i in range(n):
    grid.append(list(map(int, input().split())))

dp = [[0] * m for _ in range(n)]

dp[0][0] = grid[0][0]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue

        a = dp[i-1][j] if i > 0 else float('inf')
        b = dp[i][j-1] if j > 0 else float('inf')
        c = dp[i-1][j-1] if i > 0 and j > 0 else float('inf')

        dp[i][j] = grid[i][j] + min(a, b, c)

print(dp[n-1][m-1])
