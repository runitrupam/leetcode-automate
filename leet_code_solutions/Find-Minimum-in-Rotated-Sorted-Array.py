class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        if(N == 1):
            return nums[0]
        i = 0
        j = N - 1

        while(i < j):
            k = int((i + j) / 2)
            if(nums[k] < nums[j]):
                j = k
            else:
                i = k + 1
        return nums[i]