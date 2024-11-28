class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                if nums[i] + nums[j] == target:
                    result.extend([i,j])

        return result



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hash_table = {}

        for index,num in enumerate(nums):

            if target - num in hash_table:
                result.extend([index,hash_table[target-num]])

            if num not in hash_table:
                hash_table[num] = index

        return result