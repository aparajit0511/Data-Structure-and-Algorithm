class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0

        start,end = 0,0
        count_zero = 0

        while end < len(nums):

            if nums[end] == 0:
                count_zero += 1

            while count_zero > k:
                max_length = max(max_length,end-start)

                if nums[start] == 0:
                    count_zero -= 1

                start += 1

            end += 1

            if count_zero <= k:
                max_length = max(max_length,end-start)

        return max_length
        