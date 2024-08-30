# Time Complexity - O(NlogN)
# Space complexity - O(N) 

import heapq
class Solution:
    def lastStoneWeight(self, nums: List[int]) -> int:

        # if len(nums) == 1:
        #     return nums[0]

        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        heapq.heapify(nums)
        # print(nums)


        while True:

            if not nums:
                break
            elif len(nums) == 1:
                return abs(nums[0])

            stone1 = nums[0]
            heapq.heappop(nums)
            stone2 = nums[0]
            heapq.heappop(nums)
            # print(abs(item))
            result = abs(abs(stone1) - abs(stone2))
            # print(abs(stone1),abs(stone2),result)
            if result != 0:
                heapq.heappush(nums,-result)
            
            # print(nums)

        return result