class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        min_length = float('inf')

        for i in range(len(nums)):
            sum = 0

            for j in range(i,len(nums)):
                sum += nums[j]
                if sum >= k:
                    min_length = min(min_length,j-i+1)
                    break

        if min_length == float('inf'):
            return -1

        return min_length


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        min_length = float('inf')

        from collections import deque
        monoq = deque()

        prefix_sum = [0] * (len(nums)+1)

        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        for i in range(len(nums)+1):

            # to check if the sum b/w ith element and queue[0] is greater than k to find the subarray with atleast k sum 
            while monoq and prefix_sum[i] - prefix_sum[monoq[0]] >= k:
                min_length = min(min_length,i - monoq.popleft()) 

            while monoq and prefix_sum[i] <= prefix_sum[monoq[-1]]:
                monoq.pop() # to maintain monotonic queue

            monoq.append(i)

        return min_length if min_length != float('inf') else -1

