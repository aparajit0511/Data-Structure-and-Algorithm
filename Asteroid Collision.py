# Time Complexity - O(N)
# Space Complexity - O(N)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for i in range(len(asteroids)):
            stack.append(asteroids[i])

            while len(stack) > 1 and stack[-1] < 0 and  stack[-2] > 0:
                item = stack.pop()

                if abs(item) > stack[-1]:
                    stack[-1] = item
                elif abs(item) == stack[-1]:
                    stack.pop()
            
        return stack
