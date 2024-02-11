# Time Complexity: O(NlogN) and Space Complexity: O(N)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()

        hash_table = {}

        for i in range(len(nums)):

            if nums[i] not in hash_table:
                hash_table[nums[i]] = 1
            else:
                hash_table[nums[i]] += 1



        for key,value in hash_table.items():
            if value > (len(nums)//2):
                return key

        return 0


# Time Complexity: O(N) and Space Complexity: O(N)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hash_table = {}

        for i in range(len(nums)):

            if nums[i] not in hash_table:
                hash_table[nums[i]] = 1
            else:
                hash_table[nums[i]] += 1



        for key,value in hash_table.items():
            if value > (len(nums)//2):
                return key

        return 0
