class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        min_ = float('inf')
        
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]

                if sum >= k:
                    min_ = min(min_,j-i+1)

        return min_ if min_ != float('inf') else -1



class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        min_ = float('inf')
        sum = 0
        start = 0
        
        for i in range(len(nums)):
            sum += nums[i]

            while start < len(nums) and sum >= k:
                min_ = min(min_,i-start+1)
                sum -= nums[start]
                start += 1


        return min_ if min_ != float('inf') else -1