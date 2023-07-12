# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l = 1
        r = n
        while(l<=r):
            mid = int(l + int(r-l)/2)
            if isBadVersion(mid) == True:
                r = mid - 1
            elif isBadVersion(mid) == False:
                l = mid + 1
        return l
            
        