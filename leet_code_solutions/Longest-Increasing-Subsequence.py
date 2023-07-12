class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:        
        from bisect import bisect_left
        arr = []
        for i in range(len(A)):
            if len(arr) == 0:
                arr.append(A[i])
                
            index = bisect_left(arr,A[i])
            if index == len(arr):
                arr.append(A[i])
            else:
                arr[index] = A[i]
        return len(arr)
            
                
        
        
        '''
        TLE
        dp = [0]*len(A)
        ma_x = 0

        for i in range(len(A)):
            
            c = 0
            for j in range(0,i):
                if A[i] > A[j]:
                    c = max(c,dp[j])
            dp[i] = c + 1
            ma_x = max(ma_x, dp[i])

        return ma_x
        '''
        '''
        TLE
        n = len(nums)
        dp =[1 for x in range(n)]
        ma_x = 0
        for i in range(n-1,-1,-1):
            
            for j in range(i+1,n):
                if nums[i] < nums[j]:
                    dp[i] = max( dp[i] , dp[j] + 1)
            ma_x = max(ma_x, dp[i])
            print(dp)
        # print(dp)
        return ma_x'''
                
            