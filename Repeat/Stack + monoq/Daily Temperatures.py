# Time Complexity: O(N^2) and Space Complexity: O(N)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = []

        for i in range(len(temperatures)):
            found = 0
            for j in range(i+1,len(temperatures)):

                if temperatures[j] > temperatures[i]:
                    answer.append(j-i)
                    found = 1
                    break

            if found == 0:
                answer.append(0)

        return answer


# Time Complexity: O(N) and Space Complexity: O(N)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                # print(answer,stack,temperatures[i])
                item = stack.pop()
                answer[item] = i - item              

            stack.append(i)

        return answer

