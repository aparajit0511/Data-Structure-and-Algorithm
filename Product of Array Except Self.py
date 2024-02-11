# Time Complexity: O(N*2) and Space Complexity: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []

        for i in range(len(nums)):
            pro = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                pro = pro * nums[j]

            result.append(pro)

        return result

# Time Complexity: O(N) and Space Complexity: O(1) 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(len(nums)):
            result.append(1)

        left = 1

        for i in range(len(nums)):
            if i > 0:
                left = left * nums[i-1]
            result[i] = left

        right = 1

        for i in range(len(nums)-1,-1,-1):
            if i < len(nums)-1:
                right = right * nums[i+1]

            result[i] = result[i] * right

        return result