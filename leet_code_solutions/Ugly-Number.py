class Solution:
    def isUgly(self, n: int) -> bool:
        '''if n<=0: return False
        while n%2==0: n/=2
        while n%3==0: n/=3
        while n%5==0: n/=5
        return n==1'''
        if n == 1:
            return True
        @cache
        def rec(n):
            flag = 0
            if n == 0:
                return False
            
            if n % 2 == 0:
                if n / 2 == 1 :
                    flag = 1
                    # return True
                else:
                    if rec(int(n/2)):
                        flag = 1
            elif n % 3 == 0:
                if n / 3 == 1 :
                    flag = 1
                else:
                    if rec(int(n/3)):
                        flag = 1
                    
            elif n % 5 == 0:
                if n / 5 == 1 :
                    flag = 1
                    return True
                else:
                    if rec(int(n/5)):
                        flag = 1
            
            if flag:
                return True
            else:
                return False
        return rec(n)