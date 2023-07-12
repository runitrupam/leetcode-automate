class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        In dict we keep count of only the element found in t .
        If both dict becomes equal , we can then keep increasing i , if then the window changes , again compare both dict.
        '''
        tn = len(t)
        sn = len(s)
        if tn > sn:
            return ""
        tdp = dict()
        for j in t:
            tdp[j] = tdp.get(j,0) + 1
        i = 0
        j = 0
        sdp = dict() # window dict add element if its in t , also if e.g. sdp['a'] > tdp['a'] , sdp['a'] = tdp['a']
        sdp_orig = dict() # to store orig count of each inserted element in the window
        res = ''
        flag = 0
        # print(tdp)
        while( j <= sn and i<sn):
            # print(i,j,sdp)

            if flag == 1:
                # print(i,s[i],j,sdp,sdp_orig)
                if s[i] in sdp :
                    sdp_orig[s[i]] -=1
                    if sdp_orig[s[i]] < sdp[s[i]]:
                        sdp[s[i]] = sdp_orig[s[i]]
                        flag = 0
                    else:
                        if len(res) > len(s[i+1:j ]):
                            res = s[i+1:j  ]
                elif len(res) > len(s[i+1:j ]):
                    res = s[i+1:j  ]
                i+=1
                j-=1
            elif s[i] not in tdp :
                
                i+=1 
                j-=1
            elif j < sn and s[j] in tdp:
                sdp[s[j]] = sdp.get( s[j] , 0  ) + 1
                sdp_orig[s[j]] = sdp_orig.get( s[j] , 0  ) + 1
                if sdp[s[j]] > tdp[s[j]] :
                    sdp[s[j]] = tdp[s[j]]
                
                if tn <= (j+1-i)  and   sdp == tdp:
                    flag = 1
                    if res == '':
                        res = s[i:j+1  ]
                    elif len(res) > len(s[i:j+1  ]):
                        res = s[i:j+1  ]
            j+=1
        # print(res)
        return res    
                  