class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        '''    
        case1:
        ax1-----------ax2
              bx1-----------bx2

        case2:
        ax1-----------ax2
             bx1-bx2

        case3:
        ax1-----------ax2
                            bx1-----------bx2
        If you draw all the cases down for a and b, there can be 10 cases. However, after we swap a and b, there are only 3 cases as shown above, and all we need to do is to
        (1) find the minimum of the two endpoints
        (2) find the maximum of the two start points
        (3) overlap = (1) - (2) Note that if the result is negative, it means there is no overlap, then overlap=0, so we do overlap = max( (1)-(2), 0)

        def area(x1,y1,x2,y2):
            return (x2-x1)*(y2-y1)
        xOverlap = max(min(ax2,bx2)-max(ax1,bx1), 0)
        yOverlap = max(min(ay2,by2)-max(ay1,by1), 0)
        return area(ax1,ay1,ax2,ay2) + area(bx1,by1,bx2,by2) - xOverlap*yOverlap        
        
        
        '''
        '''
        def area(x1,y1,x2,y2):
            return (x2-x1)*(y2-y1)
        xOverlap = max(min(ax2,bx2)-max(ax1,bx1), 0)
        yOverlap = max(min(ay2,by2)-max(ay1,by1), 0)
        return area(ax1,ay1,ax2,ay2) + area(bx1,by1,bx2,by2) - xOverlap*yOverlap
        '''
        # wrong answer
        total_area = abs(by1-by2) * abs(bx1-bx2)   +    abs(ay1-ay2) * abs(ax1-ax2) 
        # print(total_area)
        s_len ,s_bread = 0 , 0
        if ay1 > by2:
            return ( total_area  )
        elif ay2 < by1:
            return ( total_area  )
        elif ax1 > bx2:
            return ( total_area  )
        elif ax2 < bx1:
            return ( total_area  )
        # else: # issue with the rectangel already inside the another
        #     if bx1 <= ax2 <= bx2 and bx1 <= ax1 <= bx2:
        #         s_len = abs(ax2 - ax1)
        #     elif by1 <= ay1 <= by2 and by1 <= ay2 <= by2 :
        #         s_bread = abs(ay2 - ay1)
        #     elif ax1 <= bx2 <= ax2 and ax1 <= bx1 <= ax2:
        #         s_len = abs(bx2 - bx1)
        #     elif ay1 <= by1 <= ay2 and ay1 <= by2 <= ay2 :
        #         s_bread = abs(by2 - by1)        
        
        else:
            
            if bx1 <= ax2 <= bx2 :
                s_len = ax2 - max( ax1 , bx1  )              
            elif bx1 <= ax1 <= bx2 :
                s_len = - ax1 + min( ax2 , bx2  ) 
            elif ax1 <= bx2 <= ax2 :
                s_len = bx2 - max( ax1 , bx1  )              
            elif ax1 <= bx1 <= ax2 :
                s_len = - bx1 + min( ax2 , bx2  ) 
            if by1 <= ay1 <= by2:
                s_bread =  min( by2 , ay2 )  - ay1
            elif by1 <= ay2 <= by2:
                s_bread = - max( by1 , ay1 )  + ay2
            elif ay1 <= by1 <= ay2:
                s_bread =  min( by2 , ay2 )  - by1
            elif ay1 <= by2 <= ay2:
                s_bread = - max( by1 , ay1 )  + by2
        # print(s_len , s_bread )
        return  total_area - abs(s_len * s_bread )