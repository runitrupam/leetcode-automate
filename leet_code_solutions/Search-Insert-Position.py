class Solution:
    def searchInsert(self, nums: List[int], t: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while( l <= r):
            mid = (l + r )// 2
            # print(mid)
            if t == nums[mid]:
                return mid
            elif t < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
            # print( l , r, mid)
        return r + 1