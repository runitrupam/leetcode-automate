class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ht = dict()
        dup_val = 0
        for i in nums:
            ht[i] = ht.get(i,0) + 1
            if ht[i] > 1:
                dup_val = i
        miss = -1
        for j in range(1,len(nums)+1):
            if j not in ht:
                miss = j
                break
        return [dup_val,miss]
        
        
        # 1 2 3 4. --> 10
        # 1 2 3 3  ---> 9. , 
        # 10 - 9 = 1