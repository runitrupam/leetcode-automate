'''
class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else 1 + (num - 1) % 9

'''

class Solution(object):
    def addDigits(self, num):
        if len(str(num)) < 2: 
            return num 
        str_num = str(num) 
        return self.addDigits(int(str_num[0]) +int(str_num[1:]))