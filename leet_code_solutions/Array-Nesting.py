class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        #X = [set() for i in range(len(nums))]
        #S = set()
        Y = set()
        max_len = 0
        for i in range(len(nums)):
            S = set()
            
            a = nums[i]
            while a not in Y:
                S.add(a)
                Y.add(a)
                a = nums[a]
            max_len = max(max_len, len(S))
        return (max_len)    
                
        