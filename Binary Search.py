# Time Complexity - O(log N)
# Space complexity - O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start + end) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1

            elif target <= nums[mid]:
                end = mid-1

        return -1
