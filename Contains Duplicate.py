## Time complexity - O(NlogN) Space Complexity - O(1)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True

        return False

## Time complexity - O(N) Space Complexity - O(N)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}

        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]]  = 1
            else:
                hash_table[nums[i]] += 1

        for key in hash_table:
            if hash_table[key] > 1:
                return True

        return False