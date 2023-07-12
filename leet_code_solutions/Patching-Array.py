class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        covered , res =0 ,0
        
        for num in nums:
            while num > covered + 1: # covered = 10 , num = 13 then res+=1 as num = 11,  res+=1 as 12 is missing
                res += 1
                covered = covered*2 + 1
                if covered >= n:
                    return res
            covered += num   # if 10 comes twice then covered = [1~10] + 10 = [1~20] 
            if covered >= n:
                return res
        while covered < n:
            covered = covered *2 + 1
            res+=1
        return res