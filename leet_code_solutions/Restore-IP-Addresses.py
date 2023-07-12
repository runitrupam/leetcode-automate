'''
# ideas:
# A valid ip address would have 4 parts separated by dots
# we iterate through `s` to insert 3 dots and separate the string into 4 segments
# for each segment, we check if it is valid
# if all 4 segments are valid, we combine those 4 segments with dots and push to the answer
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        
        # check if a given IP address segment is valid
        # 192 -> true
        # 312 -> false
        def ok(seg: str) -> bool:
            # string length > 3 is not a valid IP address segment
            # empty segment is not valid
            # if the first character is 0, we cannot have something like 0x, 0xx
            # segment is out of range
            if len(seg) > 3 or len(seg) == 0 or (seg[0] == '0' and len(seg) > 1) or int(seg) > 255:
                return False
            return True
    
        # iterate `s` - place 3 dots to have 4 segments 
        # [seg1].[seg2].[seg3].[seg4]
        # 1st dot - we just need to run it 3 times at most
        # e.g. for 255, we can place the first dot at `2.55`, `25.5` or `255.`
        for i in range(1, 4):
            # we place the 2nd dot in a similar way
            for j in range(i + 1, i + 4):
                # we place the 3rd dot in a similar way
                for k in range(j + 1, j + 4):
                    # now we can separate into 4 segments
                    seg1, seg2, seg3, seg4 = s[:i], s[i:j], s[j:k], s[k:]
                    # for each segment, check if it is valid
                    if ok(seg1) and ok(seg2) and ok(seg3) and ok(seg4):
                        # if so, we build the ip address and push to answer
                        ans.append(seg1 + "." + seg2 + "." + seg3 + "." + seg4)
        return ans

'''

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.recurse(s, ans, 0, "", 0)
        return ans
    
    def recurse(self, curr, ans, index, temp, count):
        if count > 4:
            return
        if count == 4 and index == len(curr):
            ans.append(temp)
        for i in range(1, 4):
            if index + i > len(curr):
                break
            s = curr[index:index+i]
            if (s.startswith("0") and len(s) > 1) or (i == 3 and int(s) >= 256):
                continue
            self.recurse(curr, ans, index+i, temp + s + ("." if count < 3 else ""), count+1)