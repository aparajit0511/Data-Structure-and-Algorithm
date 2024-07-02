# Time Complexity: 𝑂 ( V + E )
# Space Complexity: 𝑂 ( V + E )
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        edges = [[] for i in range(numCourses)]

        for i,j in prerequisites:
            edges[j].append(i)

        indegree = [0] * numCourses

        for i in edges:
            for j in i:
                indegree[j] += 1


        from collections import deque
        queue = deque()
        result = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)


        while queue:
            item = queue.popleft()
            result.append(item)

            for i in edges[item]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        return result if len(result) == numCourses else []