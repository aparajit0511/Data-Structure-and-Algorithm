# Time Complexity: 𝑂 ( m * n * 4^len(word) )
# Space Complexity: 𝑂 ( len(word) )

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        row , col = len(board), len(board[0])
        path = set()
        
        def backtrack(r,c,index):
            if index == len(word):
                return True

            if r < 0 or c < 0 or r >= row or c >= col or board[r][c] != word[index] or (r,c) in path:
                # print(r,row,c,col,board[r][c],word[index],path)
                return False

            path.add((r,c))

            res = backtrack(r+1,c,index+1) or backtrack(r-1,c,index+1) or backtrack(r,c+1,index+1) or backtrack(r,c-1,index+1)
            path.remove((r,c))
            return res


        for i in range(row):
            for j in range(col):
                index= 0
                if backtrack(i,j,index):
                    return True

        return False