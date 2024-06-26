# Time Complexity: 𝑂 ( m * n )
# Space Complexity: 𝑂 ( m * n )

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0

        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if (i,j) not in visited and grid[i][j] == 1:
                    area = 0
                    visited.add((i,j))

                    area = self.findIslandsArea(grid,i,j,visited,len(grid),len(grid[i]),area)

                    max_area = max(max_area,area)

        return max_area

    def findIslandsArea(self,grid,row,col,visited,i,j,area):

        from collections import deque

        queue = deque()

        queue.append((row,col))

        while queue:

            area += 1

            row,col = queue.popleft()

            for (x,y) in [(1,0),(0,1),(-1,0),(0,-1)]:
                curr_x = row + x
                curr_y = col + y

                if self.isSafe(curr_x,curr_y,i,j) and (curr_x,curr_y) not in visited and grid[curr_x][curr_y] == 1:
                    queue.append((curr_x,curr_y))
                    visited.add((curr_x,curr_y))

        return area


    def isSafe(self,x,y,i,j):
        if x >= 0 and x < i and y >= 0 and y < j:
            return True
        return False