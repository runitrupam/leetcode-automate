class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        d = dict()
        for i in range(int(c**0.5)+1):
            d[i * i] = 0 
            
        #print(d) 
        
        for j in d.keys():
            if (c - j) in  d:
                return True
        