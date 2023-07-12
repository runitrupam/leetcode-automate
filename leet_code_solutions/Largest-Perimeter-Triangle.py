class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        A= nums
        A.sort()
        
        for i in range(len(A) -1 , 1,-1):
            if A[i-1] + A[i-2] > A[i]:
                return A[i]+A[i-1]+A[i-2]
        return 0