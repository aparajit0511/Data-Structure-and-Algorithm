# Time - O(N^2) Space - O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxPro = float('-inf')
        
        for i in range(len(nums)):
            pro  = 1
            for j in range(i,len(nums)):
                pro = pro * nums[j]
                maxPro = max(maxPro,pro)

        return maxPro


# Time - O(N) Space - O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxPro = float('-inf')
        pro = 1

        for i in range(len(nums)):
            pro = pro * nums[i]
            maxPro = max(maxPro,pro)

            if pro == 0:
                pro = 1

        pro = 1

        for i in range(len(nums)-1,-1,-1):
            pro = pro * nums[i]
            maxPro = max(maxPro,pro)

            if pro == 0:
                pro = 1

        return maxPro