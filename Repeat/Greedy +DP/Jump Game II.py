# Time Complexity: O(2*N) and Space Complexity: O(N)
class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        return self.backtrack(nums,0,0,float('inf'))

    def backtrack(self,nums,start,steps,min_jump):

        if start >= len(nums)-1:
            min_jump = min(min_jump,steps)
            return min_jump


        for i in range(1,nums[start]+1):

            min_jump = self.backtrack(nums,start+i,steps+1,min_jump)

        return min_jump

# Time Complexity: O(N^2) and Space Complexity: O(N)

# concept is simple we check the jump to i+j and see how many steps it takes from i+j till the end
# then take that value in result and add +1.
# if i+j already reaches the end then we simply do a +1.
class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        
        dp = [float("inf")] * len(nums)
        dp[-1] = 0

        for i in range(len(nums)-2,-1,-1):

            for j in range(1,nums[i]+1):

                if  i + j < len(nums):
                    result = 1 + dp[i+j]

                dp[i] = min(dp[i],result)

        return dp[0]