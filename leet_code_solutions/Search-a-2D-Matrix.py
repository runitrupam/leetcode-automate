class Solution:
    def searchMatrix(self, M: List[List[int]], target: int) -> bool:
        '''
        def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
        '''





        if len(M) == 0:
            return False
        r  = len(M)
        c =len(M[0])
        row = 0
        found = 0
        while(row < r):


            if M[row][0] <= target <= M[row][-1]:
                low = 0
                high = c-1
                while(low <= high):
                    mid = (low + high) // 2
                    if M[row][mid] == target:
                        # print(row,mid)
                        return True
                    elif M[row][mid] > target:
                        high = mid - 1
                    else:
                        low = mid + 1
                return False
            else:
                row += 1
        return False