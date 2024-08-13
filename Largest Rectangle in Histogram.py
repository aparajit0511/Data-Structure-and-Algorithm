# Time Complexity - O(N)
# Space complexity - O(N)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        stack = []

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:
                # calculates area upto that height/ area of that bar
                h = heights[stack.pop()]
                # also considers width of elements that > than element stack[0]
                # example 2,1,2 width of the 0th element will also be considered
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area,h * w)
                

            stack.append(i)


        # stack will not be empty if at len(heights) an +ing order monotonic stack is created
        # to address this
        # calculate max_area here also
        while stack:
            h = heights[stack.pop()]
            w = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area,h*w)

        return max_area
        

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
