class Solution:
    def containsNearbyDuplicate(self, A: List[int], k: int) -> bool:
        
        
        d = dict()
        n = len(A)
        if k==0:
            return False
        
        
        for i,num in enumerate(A):
            
            if num in d and i - d[num] <= k : return True
            d[num] = i
        return False