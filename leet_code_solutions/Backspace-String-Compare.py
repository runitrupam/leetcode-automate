class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        sn = ''
        for i in s:
            if i == '#':
                sn = sn[:-1]
            else:
                sn = sn + i
                
        tn = ''
        for i in t:
            if i == '#':
                tn = tn[:-1]
            else:
                tn = tn + i
        
        # print(sn,tn)
        if sn == tn :
            return True
        return False