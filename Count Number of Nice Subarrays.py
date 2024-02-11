class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1


        start , end = 0 , 0
        count_odd , count_k = 0 , 0
        max_length = 0

        while end < len(nums):

            if nums[i] == 1:
                count_k = count_k + 1 

            while count_k > k:
                start += 1

                max_length = max(count_odd,max_length)

            count_odd += 1
            end += 1
