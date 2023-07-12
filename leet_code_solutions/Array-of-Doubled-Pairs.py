class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        
        d = dict()
        for i in range(len(A)):
            if A[i] not in d:
                d[A[i]] = 1
            else:
                d[A[i]] += 1
        B = sorted(d.keys())
        count = 0
        for j in B:
            if j<=0:
                count+=1
        C = B[:count]
        C.reverse()
        B = C + B[count:]
        for i in B:
            
            if d[i] != 0:
                if (i * 2) in d and d[i*2] > 0: 
                    if d[i*2] <= d[i]:
                        d[i] = d[i] - d[i*2]
                        d[i*2] = 0
                    else:
                        d[i*2] = d[i*2] - d[i]
                        d[i] = 0
                    
                else:
                    return False
                
        for i in B:
            
            if d[i] != 0:
                return False
        return True 