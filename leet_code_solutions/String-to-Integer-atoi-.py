MAX_INT = 2**31 -1
MIN_INT = 2**31 * -1

Mapping = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
}
class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.lstrip(' ')
        res = 0
        if len(s)==0:
            return 0
        sign = -1 if s[0] == "-" else 1
        if sign != 1 or s[0] == "+":
            s = s[1:]
        for ch in s:
            if ch not in Mapping:
                return self.limit(sign * res)
            res *=10
            res +=Mapping[ch]
        return self.limit(sign * res)
    
    def limit(self,n):
        if n > MAX_INT:
            return MAX_INT
        elif n<MIN_INT:
            return MIN_INT
        return n
        
        