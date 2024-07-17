# Time Complexity: 𝑂 ( m * n )
# Space Complexity: 𝑂 ( m * n )

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        from collections import deque

        queue = deque()
        visited = set()

        row ,col = len(grid) , len(grid[0])
        result = 0
        count_one = 0

        for i in range(row):
            for j in range(col):

                if grid[i][j] == 2:
                    queue.append((i,j,0))

                if grid[i][j] == 1:
                    count_one += 1

                

        while queue:

            print("hi")

            x , y , mins = queue.popleft()
            result = mins

            for (i,j) in [(1,0),(0,1),(-1,0),(0,-1)]:
                print("hi1")
                curr_x = x + i
                curr_y = y + j

                if self.isSafe(curr_x,curr_y,row,col) and grid[curr_x][curr_y] == 1 and (curr_x,curr_y) not in visited:
                    count_one -= 1
                    grid[curr_x][curr_y] = 2
                    queue.append((curr_x,curr_y,mins+1))
                    visited.add((curr_x,curr_y))

        return result if count_one == 0 else -1

    def isSafe(self,x,y,row,col):
        if x >= 0 and y >= 0 and x < row and y < col:
            return True
        return False



