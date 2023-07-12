class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        import numpy as np
        first = np.inf
        second = np.inf
        
        for i in nums:
            if i <= first:
                first = i
            elif i <= second :
                second = i
            else:
                return True
        return False
        
        
        
#         min_count = 0 
#         min_el = np.inf
#         for i in range(n-1,-1,-1):
#             if nums[i] < min_el:
#                 min_el = nums[i]
#                 min_count += 1
#             if min_count >= 3 :
#                 return True
#         return False
'''
[20,100,10,12,5,13]

min_from_left
20 20 10 10 5 5

maxFromRight 
100 100 13 13 13 13
'''
#         for i in range(n-1,-1,-1):
            
#             for j in range( i-1,-1,-1 ):
#                 if nums[j] < nums[i]:
#                     for k in range(j-1,-1,-1 ):
#                         if nums[k] < nums[j]:
#                             return True
#         return False
        
        
#         min_and_pos = []
#         import numpy as np
#         min_and_pos.append([np.inf , -1])
#         min_and_pos.append([np.inf , -1])
        
#         for i in range(1,len(nums)):
#             if nums[i-1] < min_and_pos[i][0]:
#                 min_and_pos.append(  [nums[i-1] , i-1])
#             else:
#                 min_and_pos.append( min_and_pos[i])
#         print(nums)
#         print(min_and_pos)