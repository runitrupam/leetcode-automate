class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        '''
        @cache
        def combinations(target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            ans = 0
            for num in nums:
                ans += combinations(target-num)
            return ans
        nums.sort()
        return combinations(target)
        '''
        
        
        # see the coin change 2 , for help 
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(1,target+1):
            for c in nums:
                if t - c >= 0 :
                    dp[t] += dp[t - c]
                else:
                    break
                # print('t=',t, c , dp)
        return dp[target]
        