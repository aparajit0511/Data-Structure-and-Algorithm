# Time Complexity - O(N log K)
# Space complexity - O(K)

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:

        self.nums.append(val)
        # print(self.nums)
        heap = self.nums[:self.k]

        heapq.heapify(heap)

        for num in self.nums[self.k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,num)

        return heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# ChatGPT optimized solution
import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]