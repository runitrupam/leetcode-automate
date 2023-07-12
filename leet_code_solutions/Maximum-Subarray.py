class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if max(nums) < 0:
            return max(nums)
        
        def kadanes(nums):
            curr_sum = nums[0]
            max_till_now = nums[0]
            
            for j in range(1,len(nums)):
                curr_sum = max(nums[j] ,  curr_sum + nums[j])
                max_till_now  = max(max_till_now , curr_sum)
            return max_till_now
        return kadanes(nums)
        
        
        '''
        pref_sum = 0
        
        max_sum_found = 0
        
        if max(nums) < 0:
            return max(nums)
        
        
        i = 0
        st_ind = 0
        end_ind = 0
        while(i < len(nums)):
            
            
            pref_sum += nums[i]
            
            if pref_sum < 0:
                pref_sum = 0
                st_ind = i+1
            elif pref_sum > max_sum_found:
                max_sum_found = pref_sum
                end_ind = i
            i+=1
        # print(nums[st_ind:end_ind+1])
        return max_sum_found
        '''