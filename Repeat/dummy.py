class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        nums.sort()
        count = 1
        max_count = 1

        for i in range(len(nums)-1):
            if abs(nums[i] - nums[i+1]) == 1:
                count += 1
            elif abs(nums[i] - nums[i+1]) > 1:
                count = 1

            max_count = max(max_count, count)

        return max_count



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        max_count = 0

        for x in nums:

            if x-1 not in nums:
                y = x

                while y in nums:
                    y = y + 1
                    max_count = max(max_count, y-x)


        return max_count