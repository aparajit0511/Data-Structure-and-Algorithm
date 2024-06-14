# n log n
# Time Complexity - O( N log N)
# Space complexity - O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()

        return nums[-k]

# n-k log n
# Time Complexity - O(N-K log N)
# Space complexity - O(1)

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        count = len(nums)

        while count - k > 0:
            heapq.heappop(nums)
            count = count - 1
            

        return heapq.heappop(nums)


# Time Complexity - O(N log K)
# Space complexity - O(1)
# nlogk
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]

        heapq.heapify(heap)

        for num in nums[k:]:
            # min element in the heap
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,num)

        return heap[0]

# ex -> 
# arr = [1,2,3,4,5,6]
# k = 2
# print(arr[:k])  // [1, 2]
# print(arr[k:])  // [3, 4, 5, 6]

