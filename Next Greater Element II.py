# Time Complexity - O(N*2N)
# Space Complexity - O(N)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        result = [-1] * len(nums)

        for i in range(len(nums)):
            count = 0
            j = i

            while True:
                count += 1

                index = j % len(nums)

                if nums[i] < nums[index]:
                    result[i] = nums[index]
                    break

                elif count == (len(nums)*2)+1:
                    break
                
                j=j+1

        return result

# Time Complexity - O(2N)
# Space Complexity - O(2N)

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = []
        stack = []
        hash_table = {}
        count , i = 0 ,0 
        flag = True

        while True:
            count += 1
            index = i % len(nums)

            while stack and nums[stack[-1]] < nums[index] and index not in hash_table:
                hash_table[stack[-1]] = nums[index]
                stack.pop()

            if flag:
                stack.append(index)

            if (len(nums)*2)+1 == count:
                break

            if count == len(nums):
                flag = False

            i+=1

        for i in range(len(nums)):
            if i not in hash_table:
                result.append(-1)
            else:
                result.append(hash_table[i])


        return result

