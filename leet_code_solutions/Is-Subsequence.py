class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        
        n1 = len(s)
        n2 = len(t)
        
        if n1 == n2 == 0 :
            return True
        
        if n1 > n2:
            return False
        j = 0
        for i in range(n1):
            flag = 0
            while(j < n2):
                
                if s[i] == t[j]:
                    
                    flag = 1
                    j += 1
                    break
                j += 1
            if flag == 0:
                return False
        return True
            