class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        t = n
        while( t not in seen):
            seen.add(t)

            if t == 1:
                return True
            st = str(t)
            t = sum([int(x) * int(x) for x in st] )
            # print(t)
            
        return False