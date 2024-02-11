## Time complexity - O(N^2) Space Complexity - O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    result.extend([i,j])
                    return result

        return result

## Time complexity - O(N) Space Complexity - O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_table = {}
        hash_table[nums[0]] = 0

        for i in range(1,len(nums)):
            if target - nums[i] in hash_table:
                return [hash_table[target-nums[i]],i]
            else:
                hash_table[nums[i]] = i

