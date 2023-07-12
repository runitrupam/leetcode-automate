class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            st = str(x)
            y = int( st[::-1] )
        else:
            st = str(x)
            st2 = st[1:]
            y = -1 * int(st2[::-1])
        
        if y< -(2**31) or y> (2**31 - 1):
            return 0
        return (y)    
            
        