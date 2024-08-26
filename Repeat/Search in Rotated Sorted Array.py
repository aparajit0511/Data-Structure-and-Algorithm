# Time Complexity - O(LogN)
# Space complexity - O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 4,5,1,2,3

        # 2,3,4,5,1

        # [4,5,6,7,0,1,2]

        start = 0
        end = len(nums)-1

        while start < end:
            mid = (start + end) // 2
            # print(mid)
            if nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid

        if target == nums[start]:
            return start

        pivot = start
        start , end = 0, len(nums)-1
        print(pivot)

        if target >= nums[pivot] and target <= nums[end]:
            start = pivot
        else:
            end = pivot -1

        return self.binarySearch(start,end,nums,target)

    def binarySearch(self,start,end,nums,target):
        # print(start,end)

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return -1
