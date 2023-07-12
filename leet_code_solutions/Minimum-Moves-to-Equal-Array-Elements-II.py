class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        median = nums[ int(n/2)   ]
        cost = 0
        for i in nums:
            cost +=  abs(median-i)
        return cost
        
        