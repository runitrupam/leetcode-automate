class Solution:
    def wiggleMaxLength(self, A: List[int]) -> int:
        
        '''
        see the solution for , the dp in O(N) .



        This problem is equivalent to finding the number of alternating max. and min. peaks in the array.
        
        '''
        n = len(A)
        if n < 2:
            return n
        prev_diff = A[1] - A[0]
        
        count = 2 if prev_diff !=0 else 1
        
        for i in range(2,n):
            diff = A[i] - A[i - 1]
            # print(A[i] ,  prev_diff , diff  , count)

            if diff > 0 and prev_diff <= 0:
                count +=1
                prev_diff = diff
            elif diff < 0 and prev_diff >= 0:
                count +=1
                prev_diff = diff
            
        return count