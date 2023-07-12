
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prevSum, curSum, best, zeroFound = 0, 0, 0, False
        for i in range(len(nums)):
            if nums[i] == 1: 
                curSum += 1
            if nums[i] == 0:
                best = max(prevSum + curSum, best)
                prevSum = curSum
                curSum = 0
                zeroFound = True
        return max(curSum + prevSum, best) - 1 if not zeroFound else max(curSum + prevSum, best)