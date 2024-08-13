# Time Complexity - O(N*2)
# Space complexity - O(1)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rectangle = 0

        if len(heights) == 1:
            return heights[0]

        for i in range(len(heights)):
            min_height = heights[i]
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                area = min_height * (j - i + 1)
                max_rectangle = max(max_rectangle, area)

        return max_rectangle

# Time Complexity - O(N)
# Space complexity - O(N)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_rectangle = 0

        from collections import deque
        queue = deque()

        for i in range(len(heights)):

            if queue and heights[i] < heights[queue[-1]]:
                while queue and heights[i] < heights[queue[-1]]:

                    item = queue.pop()
                    
                    if queue:
                        w = i - queue[-1] - 1
                    else:
                        w = i

                    max_rectangle = max(max_rectangle,heights[item] * ((w)))

            queue.append(i)

        while queue:
            item = queue.pop()
            
            if queue:
                w = len(heights) - queue[-1] - 1
            else:
                w = len(heights)
            max_rectangle = max(max_rectangle,heights[item] * (w))

        return max_rectangle


