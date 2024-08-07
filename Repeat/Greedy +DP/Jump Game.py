# Time Complexity: O(2*N) and Space Complexity: O(N)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        return self.backtrack(nums,0)

    def backtrack(self,nums,start):

        if start >= len(nums)-1:
            return True

        if nums[start] == 0:
            return False

        # this is basically to check every step
        # ie, if start is 3 or 3 steps 
        # it is going to check from every step
        # hence the loop goes from 1 to step 3
        for i in range(1,nums[start]+1):

            if self.backtrack(nums,start+i):
                return True


        return False

# Same approach as above but instead of recursion we are using loops

# Time Complexity: O(N*2) and Space Complexity: O(N)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums)-2,-1,-1):
            for j in range(1,nums[i]+1):
                if i + j < len(nums) and dp[i+j]:
                    dp[i] = True
                    break

        return dp[0]