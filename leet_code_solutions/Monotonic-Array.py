class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        else:
            # increasing then decr
            flag = 1
            for i in range(len(nums)):
                if i+1 < len(nums) and flag and nums[i] > nums[i+1] :
                    flag = 0
                    break
            flag2 = 1
            for i in range(len(nums)):
                if i+1 < len(nums) and flag2 and nums[i] < nums[i+1] :
                    flag2 = 0
                    break 
            if flag or flag2:
                return True
            return False
                        
                        