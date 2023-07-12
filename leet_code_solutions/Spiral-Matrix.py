class Solution:
    def spiralOrder(self, M: List[List[int]]) -> List[int]:
        
        left, right = 0, len(M[0])

        top, bottom = 0, len(M)
        res =[]

        while( left < right  and top < bottom):
            
            #top row left to right
            for i in range(left,right):
                res.append( M[top][i] )
            top += 1
            
            # go down 
            for i in range( top , bottom ):
                res.append( M[i][right-1] )
            right -= 1
            
            if not( left < right  and top < bottom   ):
                break
            
            # below row right to left
            for i in range(right - 1 , left - 1 , -1):
                res.append( M[bottom - 1][i] )
            bottom -= 1
            
            # go up from bottom to top
            for i in range(bottom -1, top -1 , -1):
                res.append( M[i][left] )
            left +=1
        return res
        
        