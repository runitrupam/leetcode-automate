class Solution:
    def submatch(self, s: str, sub: str) -> bool:
        #
        # Find subsequence in s.
        # Note: Characters of sub do not  need to be contiguous in
        # s. For example, 'abc' is a subsequence in 'aabbcc' since
		# its characters match '(a)a(b)b(c)c'.
        #
        i = -1
        for ch in sub:
            i = s.find(ch, i+1)
            if i < 0:
                return False
        return True
    
    def findLUSlength(self, strs: List[str]) -> int:
        #
        # Count each occurrence of strings in list. Strings with
        # a count of 1 are unique. A string with a greater count
        # cannot be the result since duplicates match themselves.
        #
        count = collections.Counter(strs)
        
        #
        # Sort keys placing longest at front of list. Use counter
        # keys to strip duplicate strings from list.
        #
        strs = sorted(count.keys(), key=len, reverse=True)
        
        #
        # A long string  cannot be a subsequence of a shorter one
        # so exit immediately if the first string is unique. Else
        # check remaining unique  strings for  matches inside any
        # longer strings.  Since longest are evaluated first, the
        # first non-match is the result.
        #
        for i in range(0, len(strs)):
            if count[strs[i]] == 1:
                flag = 0
                for j in range(len(strs)):
                    if j!=i and self.submatch(strs[j], strs[i]):
                        flag = 1
                        break
                if flag == 0:
                    return len(strs[i])
        return -1