class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        
        s1 = num1
        s2 = num2
        loop_count = 0
        curr_mult = ""
        res = 0
        for j in s2[::-1]:
            carry = 0
            dig2 = int(j)
            
            for k in s1[::-1]:
                dig1 = int(k)
                mul = str(dig1 * dig2 + carry)
                if len(mul) > 1:
                    carry = int( mul[0: len(mul) - 1  ])
                else:
                    carry = 0
                curr_mult = mul[-1] + curr_mult 
            curr_mult = str(carry) + curr_mult 
            # print(j ,curr_mult )
            res += int(curr_mult)
            loop_count += 1
            curr_mult =  '0' * loop_count
        return str(res)

                
                
            
            
            
        
        
        
        
        '''
        Hack of not using INT(st)
        But this q. wants the elementarty multiplications (digit by digit multiply)
        
        
        num = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        r1=0
        r2=0
        
        for i in num1:
            r1=10*r1+num[i]
        for j in num2:
            r2=10*r2+num[j]
            
        return str(r1*r2)
        '''