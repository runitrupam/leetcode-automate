class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        prev_min = prev_max = res = nums[0]
        
        for n in nums[1:]:
            curr_min = min(  n * prev_min , n * prev_max ,n    )
            curr_max = max(  n * prev_min , n * prev_max  ,n   )
            res = max(res , curr_max)
            prev_min = curr_min
            prev_max = curr_max
            
        return res