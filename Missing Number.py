# Time Complexity: O(NlogN) and Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return len(nums)


# Time Complexity: O(N) and Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            
        n = len(nums) + 1

        actual_sum = (n *(n-1)) // 2

        return actual_sum - sum