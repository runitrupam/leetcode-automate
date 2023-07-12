
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s, e, sm = 0, 0, 0
        ans = math.inf
        for e in range(len(nums)):
            sm += nums[e]
            while sm >= target:
                ans = min(ans, e-s+1)
                sm -= nums[s]
                s += 1

        return ans if ans != math.inf else 0