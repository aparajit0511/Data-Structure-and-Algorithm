# Time Complexity - O(log N)
# Space complexity - O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        start, end = 0, len(nums) - 1

        # Finding the rotation point
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        pivot = start
        start, end = 0, len(nums) - 1

        # Determine which part of the array to search in
        if target >= nums[pivot] and target <= nums[end]:
            start = pivot
        else:
            end = pivot - 1

        # Standard binary search
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1