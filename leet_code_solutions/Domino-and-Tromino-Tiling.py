
'''
dp[n]=2*d[n-1]+dp[n-3]
1 = 1
2 = 2
3 = 2 + 1   +  2(trom) = 5
4 = 4 + 1(from 2) + 3 * 2 = 11 = 2 * 5 + 1
5 = 24
6 = 53

'''
class Solution:
    def numTilings(self, n: int) -> int:
        

        dp = dict()
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        dp[4] = 11
        for i in range(5,n+1):
            dp[i] = dp[i-1] * 2 + dp[i-3]
        return dp[n] % 1000000007