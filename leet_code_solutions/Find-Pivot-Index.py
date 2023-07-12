class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left_s = 0
        right_s = 0
        if len(nums) == 1:
            return 0
        if s - nums[0] == 0:
            return 0
        for i in range(1, len(nums) ):
            left_s += nums[i-1]
            if left_s == s - left_s - nums[i] :
                return i
        return -1
            