class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        min_ = float('inf')
        
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]

                if sum >= k:
                    min_ = min(min_,j-i+1)

        return min_ if min_ != float('inf') else -1



class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        min_ = float('inf')
        sum = 0
        start = 0
        
        for i in range(len(nums)):
            sum += nums[i]

            while start < len(nums) and sum >= k:
                min_ = min(min_,i-start+1)
                sum -= nums[start]
                start += 1


        return min_ if min_ != float('inf') else -1



class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        from collections import deque

        if len(nums) == 1:
            return 1

        queue = deque()
        min_sub = float('inf')
        sum = 0

        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]

        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        for i in range(len(nums)):

            while queue and prefix_sum[i] >= k:
                item = queue[0]
                min_sub = min(i-item+1,min_sub)
                # print(min_sub)
                queue.popleft()

            while queue and nums[i] < nums[queue[-1]]:
                queue.pop()

            queue.append(i)         

        return -1 if min_sub == float('inf') else min_sub
