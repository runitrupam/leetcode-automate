class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        seen = set()
        def recur(arr   ):
            if len(arr) == n:
                res.append(arr)
                return
            
            for k in range(n):
                if nums[k] not in seen:
                    # arr.append(nums[k])
                    seen.add(nums[k])
                    recur( arr + [nums[k]] )
                    seen.remove(nums[k])
        recur([])
        return res
        # Time complexity: O(n!⋅n)   

        # Space complexity: O(n!⋅n)