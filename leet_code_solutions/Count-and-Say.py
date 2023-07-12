class Solution:
    def countAndSay(self, n: int) -> str:
        
        
        def coun(n):
            if n == '1':
                return '11'
            
            j = 1
            count = 1
            res = ''
            while(j < len(n)):
                if n[j] != n[j-1]:
                    res += str(count) + n[j-1]
                    count = 1
                else:
                    count+=1
                j+=1
            # print('in',n , j)
            res += str(count) + n[j-1]
            # print(res)
            return res
        if n == 1:
            return '1'
        result = ''
        for j in range(1,n+1):
            if j == 1:
                result = '1'
            else:
                # print(j,result)
                result = coun(result)
                
        
        return result
            
            