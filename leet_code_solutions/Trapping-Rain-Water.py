class Solution:
    def trap(self, h: List[int]) -> int:
        
        l_filled = [h[0]]
        for j in h[1:]:
            l_filled.append( max( l_filled[-1] , j   )   )
            
        r_filled = [h[-1]]
        for i in range(len(h)-2,-1,-1):
            r_filled.append( max(r_filled[-1] , h[i]  ) )
        r_filled = r_filled[::-1]
        
        value = []
        for i in range(len(h)):
            value.append(  min( l_filled[i] , r_filled[i]  )   - h[i]     )
        return sum(value)
        