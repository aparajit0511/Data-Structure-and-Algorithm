# Time Complexity: O(NlogN) and Space Complexity: O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        nums.sort()

        max_count = 1
        count = 1

        for i in range(len(nums)-1):
            if abs(nums[i] - nums[i+1]) == 1:
                count +=1
            elif abs(nums[i] - nums[i+1]):
                count = 1
            max_count = max(count,max_count)
                
        return max_count


# Time Complexity: O(N) and Space Complexity: O(1)
# Leetcode discuss solution - https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0

        nums = set(nums)

        for value in nums:
            if value - 1 not in nums:
                y = value + 1

                while y in nums:
                    y += 1

                max_count = max(max_count,y - value)

        return max_count
        