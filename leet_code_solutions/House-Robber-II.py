class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        def _rob(A):
            d = [0 for i in range(len(A))]
            n = len(A)

            d[0] = A[0]
            if n == 1 :
                return A[0]
            d[1] = max(A[1],A[0])


            for i in range(2,n):

                d[i] = max(  d[i-1] , d[i-2] + A[i]    )
            # print(d)
            return d[-1]
        return max(_rob(nums[1:]) , _rob(nums[:-1])  )