# Time Complexity: 𝑂 ( N ^ 2 )
# Space Complexity: 𝑂 (1) # dont count result array


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        

        result = []

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    result.append(nums[i])


        return result

# Time Complexity: 𝑂 ( N  )
# Space Complexity: 𝑂 (N)

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        hash_table = {}
        result = []

        for i in range(len(nums)):

            if nums[i] not in hash_table:
                hash_table[nums[i]] = 1
            else:
                result.append(nums[i])

        return result


# Time Complexity: 𝑂 ( N )
# Space Complexity: 𝑂 (1)

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1  # Convert value to index
            if nums[index] < 0:
                result.append(abs(nums[i]))
            else:
                nums[index] = -nums[index]

        return result
