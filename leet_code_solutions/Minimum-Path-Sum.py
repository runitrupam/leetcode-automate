class Solution:
    def minPathSum(self, G: List[List[int]]) -> int:
        r =len(G) 
        c =len(G[0])
        
        dp = [[G[j][i] for i in range(c)] for j in range(r) ]
        
        for i in range(1,r):
            dp[i][0] += dp[i-1][0]
            
        for j in range(1,c):
            dp[0][j] += dp[0][j-1]
        
        # print(dp)
        
        for i in range(1,r):
            for j in range(1,c):
                
                dp[i][j] += min( dp[i-1][j] , dp[i][j-1])
        return dp[r-1][c-1]
            
        
        
        