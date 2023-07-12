class NumArray:

    def __init__(self, nums: List[int]):
        
        global prefix_sum
        prefix_sum = nums # global variable of class
        for i in range(len(nums) - 1):
            prefix_sum[i+1] += prefix_sum[i] # to make gloabl
            

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return prefix_sum[right]
        else:
            return prefix_sum[right] - prefix_sum[left-1]
         

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)