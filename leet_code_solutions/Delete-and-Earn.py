class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        
        dp = dict()
        for i in nums:
            dp[i] = dp.get(i,0) + 1
        
        li = list(dp.keys())
        li.sort()
        # print(li)
        
        res = list()
        res.append( li[0] * dp[li[0]]   )
        
        for j in range(1,len(li)):
            
            if li[j] - li[j-1] == 1:
                if j > 1:
                    res.append(  max(  li[j] * dp[li[j]] + res[j-2] , res[j-1]       )    )
                else:
                    res.append(   max(  li[j] * dp[li[j]] , res[j-1]  )   )
            else:
                res.append( li[j] * dp[li[j]] + res[j-1])
        return res[-1]        