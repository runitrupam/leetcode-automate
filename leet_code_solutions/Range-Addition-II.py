class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        X_d = dict()
        
        Y_d = dict()
        for i in range(0,m):
            X_d[i] = 0
        for i in range(0,n):
            Y_d[i] = 0
        for i,j in ops:
            k = 0
            
            while k < i:
                X_d[k] += 1
                k+=1
            #x_count = X_d[k-1]  
            k = 0
            while k<j:
                Y_d[k] += 1
                k+=1
            #y_count = Y_d[k-1]    
            #ma_x = max(ma_x,x_count,y_count)    
        print(X_d,Y_d)
        count_x = 0
        count_y = 0
        for i in X_d.keys():
            if X_d[i] == X_d[0]:
                count_x +=1 
        for i in Y_d.keys():
            if Y_d[i] == Y_d[0]:
                count_y +=1  
        if X_d[0] == Y_d[0]:
            return count_x * count_y
        