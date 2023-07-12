'''

2 - 1 1
3 - 1 2
4 - 2 2
5 - 3 2
6 - 3 3  
7 - 3 2 2
8 - 3 3 2
9 - 3 3 3
10 - 3 3 4
11 - 3 3 3 2
11
12 - 3 3 3 3

'''
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 3:
            return 2
        dp = [1 for i in range(n+1+5)]
        
        dp[2] = 1
        dp[3] = 3
        dp[4] = 4
        dp[5] = 6
        
        for i in range(6 , n+1):
            dp[i] = 3 * dp[i-3]
        return dp[n]
        '''
        if(n<=3):
            return n-1
        n3=n//3
        r3=n%3
        if(r3==0):
            return 3**n3
        if(r3==1):
            r3=4
            n3-=1
        return r3*(3**n3)
        '''
        