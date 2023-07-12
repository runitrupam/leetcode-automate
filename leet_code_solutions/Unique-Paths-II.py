class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        dp = [ [0 for x in range(c)] for y in range(r)   ]
        for i in range(0,r):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                break
            else:
                dp[i][0] = 1
        for j in range(0,c):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
                break
            else:
                dp[0][j] = 1   
        
        
        # print(dp)
        
        for i in range(1,r):
            
            for j in range(1,c):
                # print(i,j)
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[r-1][c-1]