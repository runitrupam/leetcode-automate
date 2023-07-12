from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        per_sq = [k*k for k in range(101)]
        set_per_sq = set(per_sq)
        
        
        @cache
        def find(count , n):
            
            if count == 1 :
                return n in set_per_sq
            for v in per_sq:
                if v > n:
                    break
                if find(count - 1 , n - v):
                    return True
            
            return False
        
        
        for count in range(1,n+1):
            
            if find(count , n):
                return count
            