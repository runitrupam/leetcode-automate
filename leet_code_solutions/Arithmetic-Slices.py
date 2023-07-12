class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        '''
        there are 2 parts , 
        1st --> len of arithmnetic series , so total substring of length n 
        2nd --> len of arithmentic series
        
        
        '''
        
        '''
        dp = dict()
        if len(nums) <=2:
            return 0
        dp[0] = 0
        dp[1] = 0
        dp[2] = 0
        dp[3] = 1
        dp[4] = 2 * dp[3] + 1
        dp[5] = 2 * dp[4] + 1 - dp[3]
        count = 2
        diff = nums[1] - nums[0]
        res = 0
        for i in range(2,len(nums)):
            
            if nums[i] - nums[i-1] == diff:
                count +=1
                if count not in dp:
                    dp[count] = dp[count - 1] * 2 + 1 - dp[count - 2]
            else:
                res += dp[count]
                count = 2
                diff = nums[i] - nums[i-1]
        res += dp[count]
        return res
            
        '''

        le=len(A)
        l=[0]*(le)
        for i in range(2,le):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                l[i]=1+l[i-1]
        return sum(l)