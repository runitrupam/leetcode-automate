class Solution:
    def convert(self, s: str, n: int) -> str:
        L = [''] * n
        pos = -1


        count = 0
        for j in s:
            
            pos += 1
            if pos >= n and count < n -2:
                count += 1
                L[n-count-1] = L[n-count-1] + j
                
            elif pos >= n :
                count = 0 
                pos = 0

            if pos < n:
                L[pos] = L[pos] + j
            # print(pos , count , L) 
        return ''.join(L)
