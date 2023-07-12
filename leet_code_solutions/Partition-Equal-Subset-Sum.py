

'''
        If we are able to divide the array, we can split the total sum into equal halfs. That means the sum must be an even number. Now we only search for half the value of the total sum. If any subarray is able to form target sum, we can split the array into 2 halfs.

The question then becomes same as subset with target sum k.
'''
class Solution: # top down + memoization
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        
        if target % 2: return False # sum must be even number to divide it nums into 2 parts
        
        target //= 2
        A = nums

        # if we are able to split the array into two subsets with equal sums, then they will sum to sum(nums)//2
        # thus, we can check if we can sum to sum(nums)//2 with numbers from nums
        s = sum(nums)
        if s % 2: # if the sum of the numbers is odd then we cannot split into two subsets with equal sums
            return False
        dp = [True] + [False]*(s//2) # dp[i] keeps track of whether or not we can sum to i with elements in nums
        for num in nums:
            for i in range(s//2-num,-1,-1): # go backwards through dp
                if dp[i]: # if we can sum to i
                    dp[i+num] = True # then now we can sum to i + num
        return dp[-1] # see if we can sum to s//2

        '''@cache
        def dfs(target, i):
            if target == 0: return True
            if target < 0: return False
            if i == len(nums): return False
            
            op1 = dfs(target - nums[i], i + 1)
            if op1: return True
            return dfs(target, i + 1)
        
        return dfs(target, 0)'''
