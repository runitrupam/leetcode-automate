class Solution:
    def jump(self, A: List[int]) -> int:

        curr_j = A[0] # curr jump
        i = 0
        n = len(A)
        totaljump = 0
        while( i < n-1):
            if i+curr_j >= n-1:
                # print( i ,i+curr_j , n  )
                return totaljump + 1

            new_j = 0
            new_i = -1
            for j in range( 1,curr_j + 1 ):

                if A[ i + j] - (curr_j - j) > new_j :
                    new_j = A[i + j] - (curr_j - j)
                    # new_i = j
            # print(  i , i + curr_j , new_j)
            i = i + curr_j
            curr_j = new_j
            totaljump += 1
            
        return totaljump  

                



        