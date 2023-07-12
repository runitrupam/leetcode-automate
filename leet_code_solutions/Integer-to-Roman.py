class Solution:
    def intToRoman(self, num: int) -> str:
        
        n = num
        res  = ''
        while(n):
            # print(n,res)
            if n >= 1000:
                res += n//1000 * 'M'
                n = n -  n//1000 * 1000
            if n >= 900 :
                res += 'CM'
                n = n - 900
            if n >= 500:
                res += n//500 * 'D'
                n = n -  n//500  * 500
            if n >= 400 :
                res += 'CD'
                n = n - 400 ####### C done
            if n >= 100:
                res += n//100* 'C'
                n = n -  n//100  * 100
            if n >= 90 :
                res += 'XC'
                n = n - 90
            if n >= 50:
                res += n//50 * 'L'
                n = n -  n//50  * 50
            if n >= 40 :
                res += 'XL'
                n = n - 40 ###### X done
            if n >= 10:
                res += n//10 * 'X'
                n = n -   n//10  * 10
            if n >= 9 :
                res += 'IX'
                n = n - 9
            if n >= 5:
                res += n//5 * 'V'
                n = n -  n//5  * 5
            if n >= 4 :
                res += 'IV'
                n = n - 4 ###### I done
            if n >= 1:
                res += n * 'I'
                n = 0
        return res
            
        