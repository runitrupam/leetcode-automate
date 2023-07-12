class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadanes(nums):
            curr_sum = nums[0]
            max_till_now = nums[0]
            
            for j in range(1,len(nums)):
                curr_sum = max(nums[j] ,  curr_sum + nums[j])
                max_till_now  = max(max_till_now , curr_sum)
            return max_till_now
           
        #there will be 2 case
        #case 1 : our max subarray is not wrapping i.e not circular
        #case 2: our max subarray is wrapping i.e circular
        
        # case 1 is easy to find
        # to find case 2 what we can do is if we multiply each nums element by -1 and 
        # on that find kadanes then we will get sum of elements which is not part of maxsubarray in case2 (not part because we negate)
        # now subtract this newmax in case 2 from total nums sum, we get wrapping sum
        # max of case1 and case is our ans
        
        non_wrapping_sum = kadanes(nums)
        if non_wrapping_sum < 0 :
            return non_wrapping_sum
        
        min_substring_sum = - kadanes([-1 * n for n in nums]) # 1st convert whole array to -ve , then get the max substring sum from it 
        wrapping_sum = sum(nums) - min_substring_sum
        return max(  non_wrapping_sum , wrapping_sum )