# Time Complexity - O(M*N)
# Space complexity - O(M*N)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        hashSet1 = set()

        # column wise
        for i,row in enumerate(board):
            hashSet1 = set()
            for j,col in enumerate(row):
                if board[j][i] != ".":
                    if board[j][i] not in hashSet1:
                        hashSet1.add(board[j][i])
                    else:
                        return False


        # row wise
        for i,row in enumerate(board):
            hashSet1 = set()
            for j,col in enumerate(row):
                if board[i][j] != ".":
                    if board[i][j] not in hashSet1:
                        hashSet1.add(board[i][j])
                    else:
                        return False


        # 3*3
        for sub_row in range(0, 9, 3):
            for sub_col in range(0, 9, 3):
                hashSet1 = set()
                for row in range(sub_row, sub_row + 3):
                    for col in range(sub_col, sub_col + 3):
                        if board[row][col] != ".":
                            if board[row][col] not in hashSet1:
                                hashSet1.add(board[row][col])
                            else:
                                return False

        return True


