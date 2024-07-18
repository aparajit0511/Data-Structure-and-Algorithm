# Time Complexity: O(NlogN) and Space Complexity: O(1)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()
        max_count = 1
        count = 1

        for i in range(len(nums)-1):

            if abs(nums[i] - nums[i+1]) == 1:
                count += 1
            elif abs(nums[i] - nums[i+1]) > 1:    
                count = 1
            max_count = max(max_count,count)
                

        return max_count


# Time Complexity: O(N) and Space Complexity: O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_count = 0

        nums = set(nums)

        for x in nums:
            if x-1 not in nums:
                y = x + 1

                while y in nums:
                    y += 1

                max_count = max(max_count,y-x)

        return max_count
