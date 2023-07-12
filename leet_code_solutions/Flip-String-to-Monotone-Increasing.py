class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        cnt_0 = s.count('0')
        cnt_1 = s.count('1')
        #print(s[3:].count('0'))
        one_so_far = 0
        mi_n = min(cnt_0,cnt_1)
        for i in range(len(s)):
            
            if s[i] == '1':
                #cnt_of_0 = s[i:].count('0')
                mi_n = min(mi_n,cnt_0 + one_so_far)
                one_so_far = one_so_far + 1
            if s[i] == '0':
                cnt_0 -= 1
        return (mi_n)   