class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        
        li = s.split(' ')
        li=li[::-1]
        # print(li)
        res = []
        for j in li:
            if j != '':
                res.append(j)
        return ' '.join(res)