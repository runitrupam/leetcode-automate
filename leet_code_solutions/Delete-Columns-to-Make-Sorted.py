class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        n = len(strs[0])

        i = 0
        res = 0
        while(i<n):
            for j in range(len(strs)-1):
                if strs[j][i] > strs[j+1][i]:
                    res += 1
                    break
            i += 1
        return res