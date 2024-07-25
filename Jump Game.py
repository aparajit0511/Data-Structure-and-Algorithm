class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.backtrack(nums, 0)

    def backtrack(self, nums: List[int], start: int) -> bool:
        if start >= len(nums) - 1:
            return True

        if nums[start] == 0:
            return False

        for i in range(1, nums[start] + 1):
            if self.backtrack(nums, start + i):
                return True

        return False