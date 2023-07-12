'''
if mid is even , then compare with A[mid] , A[mid+1] and set l = mid + 1
if mid is odd , then compare with A[mid-1] , A[mid+1] and set l = mid + 1
'''
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        low = 0
        high = len(nums) - 1
        
        if nums[0] != nums[1]:
            return nums[0]
 
        if nums[high] != nums[high - 1]:
            return nums[high]
        
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif (nums[mid] == nums[mid + 1] and mid % 2 == 0) or (nums[mid] == nums[mid - 1] and mid % 2 != 0):
                low = mid + 1
            else:
                high = mid - 1
        return nums[low]


'''

# mid^1 = mid xor 1 ==== will inc mid by 1 if even , or dec by 1 if odd.
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-2
        while end>=start:
            mid = (end+start)//2
            if nums[mid] == nums[mid^1]: # will change
                start = mid+1
            else:
                end = mid-1
        return nums[start]
