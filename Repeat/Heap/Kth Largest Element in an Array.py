# Time Complexity - O( N log N)
# Space complexity - O(1)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort(reverse=True)

        return nums[k-1]


# Time Complexity - O(N log K)
# Space complexity - O(1)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        print(heap)

        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,num)


        return heap[0]