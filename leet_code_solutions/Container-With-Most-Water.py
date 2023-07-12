class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        max_so_far = 0
        i = 0
        j = len(height)-1
        a = 0
        b = 0
        while(i <j and i<len(height)-1 and j > 0):
            max_so_far = max(max_so_far,(j-i)* min(height[i],height[j] ) )
            if height[i] < height[j] :
                i+=1
            else:
                j-=1
            
            #print(k,a,'r =',r,b,'ind=', i,j,max_so_far)    

            
        return max_so_far        
        
        