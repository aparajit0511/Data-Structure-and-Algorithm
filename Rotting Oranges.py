# Time Complexity: 𝑂 ( m * n )
# Space Complexity: 𝑂 ( m * n )

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        queue = deque()
        
        rotten_time = 0

        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if (i,j) not in visited and grid[i][j] == 1:
                    visited.add((i,j))
                elif grid[i][j] == 2:
                    queue.append((i,j,rotten_time))


        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 2:
                    rotten_time = self.checkRotting(queue,grid,i,j,visited,rotten_time,len(grid),len(grid[i]))


        return -1 if visited else rotten_time


    def checkRotting(self,queue,grid,row,col,visited,rotten_time,i,j):

        while queue:
            row,col,rotten_time = queue.popleft()

            for (x,y) in [(1,0),(0,1),(-1,0),(0,-1)]:
                curr_x = row + x
                curr_y = col + y

                if self.isSafe(curr_x,curr_y,i,j)  and grid[curr_x][curr_y] == 1:
                    grid[curr_x][curr_y] = 2
                    visited.remove((curr_x,curr_y))
                    queue.append((curr_x,curr_y,rotten_time+1))


        return rotten_time


    def isSafe(self,x,y,i,j):
        if x >= 0 and x < i and y >= 0 and y < j:
            return True
        return False