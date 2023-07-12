class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        MOD = 10 ** 9 + 7
        stack = []
        sum_of_minimums = 0;

        for i in range(len(arr) + 1):
            
            # when i reaches the array length, it is an indication that
            # all the elements have been processed, and the remaining
            # elements in the stack should now be popped out.

            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):

                # Notice the sign ">=", This ensures that no contribution
                # is counted twice. right_boundary takes equal or smaller 
                # elements into account while left_boundary takes only the
                # strictly smaller elements into account

                mid = stack.pop()
                left_boundary = -1 if not stack else stack[-1]
                right_boundary = i

                # count of subarrays where mid is the minimum element
                count = (mid - left_boundary) * (right_boundary - mid)
                sum_of_minimums += (count * arr[mid])

            stack.append(i)
        
        return sum_of_minimums % MOD

        
        '''
        
        n = len(A)
        dp = [[0] * n  for i in range(n)]
        print(dp)
        s = 0
        for i in range(n):
            dp[i][i] = A[i]
            s += dp[i][i]
            for j in range(i+1,n):
                # print(i , j)
                dp[i][j] = min(   A[j],  dp[i][j-1]  )
                s += dp[i][j]
        print(dp)
        return s%(1000000007 )'''