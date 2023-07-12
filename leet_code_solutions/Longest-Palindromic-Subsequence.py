class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n)] for x in range(n)  ]
        
        for i in range(n-1,-1,-1):
            
            dp[i][i] = 1
            for j in range(i+1,n):
                
                
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(  dp[i+1][j] , dp[i][j-1]    )
        return dp[0][n-1]
            
        
        
        '''
        @cache
        def recur(l,r):
            
            if l > r :
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                return 2 + recur(l+1,r-1)
            return max(   recur(l,r-1) ,recur(l+1,r)   )
            
            
        return recur(0,len(s) - 1)
        '''
        