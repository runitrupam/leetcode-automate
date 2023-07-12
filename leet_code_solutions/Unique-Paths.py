class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        r = m
        c = n
        dp = [ [1 for x in range(c)] for y in range(r)   ]
        # print(dp)
        
        for i in range(1,r):
            
            for j in range(1,c):
                # print(i,j)
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[r-1][c-1]