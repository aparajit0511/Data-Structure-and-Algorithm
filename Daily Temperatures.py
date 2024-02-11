# Time Complexity - O(N^2)
# Space Complexity - O(1)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = []

        for i in range(len(temperatures)):
            flag = 0

            for j in range(i+1,len(temperatures)):

                if temperatures[i] < temperatures[j]:
                    result.append(j-i)
                    flag = 1
                    break
            
            if flag == 0:
                result.append(0)

        return result


# Time Complexity - O(N)
# Space Complexity - O(N)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        from collections import deque

        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                item = stack.pop()
                result[item] = i-item

            stack.append(i)

        return result
