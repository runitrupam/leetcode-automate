class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0 for i in range(len(s) +1)]
        
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        
        for i in range(2,len(s)+1):
            
            if 0 < int(s[i-1]) <= 9:
                dp[i] += dp[i-1]
            if  10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]
            
        
        
        '''
        # best way using a rec. with memorization
        @cache
        def noofways(s , i ,j):
            # print(s[i:j+1])
            if i == j:
                return 1
            if s[i] == '0':
                return 0
            
            if j - i == 1:
                return 1
            
            # if 0 < int(s[i]) <= 9:
            #     dp[i] += dp[i-1]
            # if 10 <= int(s[i-2:i]) <= 26:
            #     dp[i] += dp[i-2]
            
            if int(s[i]) >= 3:
                return noofways(s , i+1 ,j)
            elif int(s[i]) == 2 and int(s[i+1]) <= 6:
                return noofways(s , i+2 ,j) + noofways(s , i+1 ,j)
            elif int(s[i]) == 1:
                return noofways(s , i+2 ,j) + noofways(s , i+1 ,j)
            elif int(s[i]) >= 1 and int(s[i+1]) > 6:
                return noofways(s , i+1 ,j)
        return noofways(s , 0 ,len(s))'''