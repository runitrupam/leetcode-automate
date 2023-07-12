class Solution:
    def search(self, A: List[int], target: int) -> int:
        
        if target < A[0] or target > A[-1]:
            return -1
        l = 0
        r = len(A) - 1
        while(l <= r):
            mid = int(l +  int(r - l)/2 ) 
            if A[mid] == target :
                return mid
            # elif l == r:
            #     return -1
            elif A[mid] > target :
                r = mid - 1
            else:
                l = mid + 1
        return -1
            