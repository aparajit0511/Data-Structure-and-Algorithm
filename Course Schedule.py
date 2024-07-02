# Time Complexity: 𝑂 ( V + E )
# Space Complexity: 𝑂 ( V + E )
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # creating edges the size of the numCourses
        # size 2 will have [[],[]] edge array
        edges = [[] for i in range(numCourses)]

        # creating e dges j points to i
        for i,j in prerequisites:
            edges[j].append(i)


        # indegree array 
        # indegree default value marked as 0
        indegree = [0] * numCourses

        # indegree 0 is the starting point
        for i in edges:
            for j in i:
                indegree[j] += 1


        from collections import deque
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        result = []

        while queue:
            item = queue.popleft()
            result.append(item)

            for i in edges[item]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)           

        if len(result)==0 or len(result) < numCourses:
            return False

        return True