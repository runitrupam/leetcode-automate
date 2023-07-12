class Solution:
    def minimumTotal(self, T: List[List[int]]) -> int:
        if len(T) == 1 : 
            return T[0][0]
        
        r = len(T)
        c = len(T[0])
        for i in range(1,r):
            
            for j in range(len(T[i])):
                mi_n = 2000000
                if j < len(T[i-1]):
                    mi_n = min(mi_n, T[i-1][j]  )
                if j - 1 >= 0:
                    mi_n = min(mi_n,T[i-1][j-1])
                T[i][j] += mi_n
                
        # print(T)
        return min(T[-1])