'''
deque([15, 3, 4, 5, 6, 7]) 0
deque([3, 4, 5, 6, 7, 16, 13, 18, 19, 20, 21]) 1
deque([4, 5, 6, 7, 16, 13, 18, 19, 20, 21, 8, 9]) 1
deque([5, 6, 7, 16, 13, 18, 19, 20, 21, 8, 9, 10]) 1
deque([6, 7, 16, 13, 18, 19, 20, 21, 8, 9, 10, 11]) 1
deque([7, 16, 13, 18, 19, 20, 21, 8, 9, 10, 11, 12]) 1
deque([16, 13, 18, 19, 20, 21, 8, 9, 10, 11, 12, 13]) 1
deque([13, 18, 19, 20, 21, 8, 9, 10, 11, 12, 13, 22]) 2
deque([18, 19, 20, 21, 8, 9, 10, 11, 12, 13, 22, 35, 15]) 2
deque([19, 20, 21, 8, 9, 10, 11, 12, 13, 22, 35, 15, 23, 24]) 2
deque([20, 21, 8, 9, 10, 11, 12, 13, 22, 35, 15, 23, 24, 25]) 2
deque([21, 8, 9, 10, 11, 12, 13, 22, 35, 15, 23, 24, 25, 26]) 2
deque([8, 9, 10, 11, 12, 13, 22, 35, 15, 23, 24, 25, 26, 27]) 2
deque([9, 10, 11, 12, 13, 22, 35, 15, 23, 24, 25, 26, 27]) 2
deque([10, 11, 12, 13, 22, 35, 15, 23, 24, 25, 26, 27]) 2
deque([11, 12, 13, 22, 35, 15, 23, 24, 25, 26, 27]) 2
deque([12, 13, 22, 35, 15, 23, 24, 25, 26, 27]) 2
deque([13, 22, 35, 15, 23, 24, 25, 26, 27]) 2
deque([22, 35, 15, 23, 24, 25, 26, 27]) 2
deque([35, 15, 23, 24, 25, 26, 27, 28]) 3
deque([15, 23, 24, 25, 26, 27, 28, 36]) 3
deque([23, 24, 25, 26, 27, 28, 36]) 3
deque([24, 25, 26, 27, 28, 36, 29]) 3
deque([25, 26, 27, 28, 36, 29, 30]) 3
deque([26, 27, 28, 36, 29, 30, 31]) 3
deque([27, 28, 36, 29, 30, 31, 32]) 3
deque([28, 36, 29, 30, 31, 32, 33]) 3
deque([36, 29, 30, 31, 32, 33, 34]) 4



'''

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        moves = 0
        q = collections.deque([1])
        visited = [[False for _ in range(n)] for _ in range(n)]
        visited[n-1][0] = True
        while q:
            size = len(q) # run inner for loop , only for the inserted elements size
            for i in range(size):
                currBoardVal = q.popleft()
                if currBoardVal == n*n:
                    return moves
                for diceVal in range(1, 7):
                    if currBoardVal + diceVal > n*n:
                        break
                    pos = self.findCoordinates(currBoardVal + diceVal, n)
                    row, col = pos
                    if not visited[row][col]:
                        visited[row][col] = True
                        if board[row][col] == -1:
                            q.append(currBoardVal + diceVal)
                        else:
                            q.append(board[row][col])
                # print(q,moves)
            moves += 1
        return -1
    
    def findCoordinates(self, curr: int, n: int) -> Tuple[int, int]:
        row = n - (curr - 1) // n - 1
        col = (curr - 1) % n
        if row % 2 == n % 2:
            return (row, n - 1 - col)
        else:
            return (row, col)