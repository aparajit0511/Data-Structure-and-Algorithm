class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        queue = deque()
        result = []

        for i,value in enum(nums):
            # check if the queue is monotonic
            while queue and nums[queue[-1]] <= value:
                queue.pop()

            # maintain the monotonic queue
            queue.append(i) 


            # remove first element if its outside the window
            if queue[0] == i-k:
                queue.popleft()

            if i >= k-1:
                result.append(nums[queue[0]])

        return result