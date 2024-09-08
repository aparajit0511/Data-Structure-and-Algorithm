
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        start ,end = 0, k-1

        result.append(max(nums[start:end+1]))
        end += 1
        start += 1
        while end < len(nums):

            if end-start+1 == k:
                result.append(max(nums[start:end+1]))
                start+=1
            end += 1

        return result


# Time Complexity - O(N)
# Space complexity - O(N)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        queue = deque()
        result = []

        for i in range(len(nums)):

            # check if the queue is monotonic in decreasing order
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()


            queue.append(i)

            # remove first element if its outside the window
            if queue[0] == i-k:
                queue.popleft()

            if i >= k-1:
                result.append(nums[queue[0]])

        return result