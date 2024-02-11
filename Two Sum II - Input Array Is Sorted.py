# Time Complexity: O(N*N) and Space Complexity: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i+1,j+1]

        return []

# Time Complexity: O(N) and Space Complexity: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0,len(nums)-1

        while left < right:
            value = nums[left] + nums[right]
            if value == target:
                return [left+1,right+1]
            elif value > target:
                right -=1
            elif value < target:
                left +=1

        return []