class Solution:
    def calculate(self, s: str) -> int:
        digits = set( [x for x in '0123456789']  )
        # print(digits)
        def rec(s,i,j):
            res = 0
            prev_sign = 1
            while i <= j:
                if s[i] == ' ':
                    i += 1
                elif s[i] == '(' :
                    new_i = i + 1
                    new_j = j

                    ob = 1
                    for k in range(i+1,j+1):
                        if s[k] == ')':
                            ob -= 1
                            if ob == 0:
                                new_j = k - 1
                                break
                        if s[k] == '(':
                            ob += 1
                    res += rec(s , new_i , new_j)    * prev_sign
                    i = new_j + 2
                    if i >= j:
                        break
                else:
                    num = 0
                    tmp = 0
                    for k in range(i , j+1):
                        if s[k] in digits:
                            num = num * 10 + int(s[k])
                        elif s[k] == '(':
                            i = k
                            break
                        elif s[k] == '+':
                            tmp += num * prev_sign
                            prev_sign = 1
                            num = 0
                        elif s[k] == '-':
                            tmp += num * prev_sign
                            prev_sign = -1
                            num = 0
                    # print(k)
                    if k >= j:
                        i = k + 1
                    tmp += num * prev_sign
                    res += tmp
            return res
                
            
            
        return rec(s,0,len(s) - 1)
            