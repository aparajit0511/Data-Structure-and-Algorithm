# Time Complexity: 𝑂 ( m * n )
# Space Complexity: 𝑂 ( m * n )
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        count_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # print(i,j)

                if (i,j) not in visited and grid[i][j] == '1':
                    visited.add((i,j))
                    self.countIslands(grid,i,j,visited,len(grid),len(grid[i]))
                    # print(visited)
                    count_islands += 1

        return count_islands

    def countIslands(self,grid,row,col,visited,i,j):

        from collections import deque

        queue = deque()
        queue.append((row,col))

        while queue:

            row,col = queue.popleft()
            # print(row,col)

            for (x,y) in [(1,0),(0,1),(-1,0),(0,-1)]:
                curr_x = row + x
                curr_y = col + y
                if self.isSafe(curr_x,curr_y,i,j) and grid[curr_x][curr_y] == '1' and (curr_x,curr_y) not in visited:
                    queue.append((curr_x,curr_y))
                    visited.add((curr_x,curr_y))

    def isSafe(self,x,y,i,j):
        if x >= 0 and x < i and y >= 0 and y < j:
            return True
        return False
