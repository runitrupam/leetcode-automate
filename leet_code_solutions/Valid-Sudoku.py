class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        # for b in board:
        #     print(b)
        def is_unit_valid(L):
            dp = set()
            for x in L:
                if x == '.':
                    continue
                if x in dp:
                    return False
                else:
                    dp.add(x)
            return True
        def is_square_valid(board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                    if not is_unit_valid(square):
                        return False
            return True
        for i in range(len(board)):
            dp = set()
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                if board[j][i] in dp:
                    return False
                else:
                    dp.add(board[j][i])
            dp = set()
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in dp:
                    return False
                else:
                    dp.add(board[i][j])
        return is_square_valid(board)