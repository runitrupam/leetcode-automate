class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]  + nums
        
        for i in range( 2 , len(dp)):
            dp[i] = max( dp[i-2] + dp[i] , dp[i-1]  )
            # print(dp)
        return dp[-1]