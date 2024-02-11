class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        count = 0

        for i in range(len(nums)):
            sum = 0
            if nums[i] == goal:
                count +=1

            sum += nums[i]

            for j in range(i+1,len(nums)):
                sum += nums[j]

                if sum == goal:
                    count += 1

        return count

# Working Solution 
# Time and space - O(N)
class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:

        result = 0
        currentSum = 0
        hash_table = {0:1}  #no of times sum 0 appearing

        for i in range(len(nums)):
            currentSum += nums[i]

            if currentSum - k in hash_table:
                result += hash_table[currentSum-k]

            hash_table[currentSum] = hash_table.get(currentSum,0) + 1

        return result

# Not working two pointer solution
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        start ,end = 0 , 0
        current_sum = 0

        max_length = float('-inf')

        while end < len(nums):
            current_sum = current_sum + nums[end]
            end += 1

            while start < end and current_sum >= goal:
                current_sum = current_sum - nums[start]
                start+=1

                max_length = max(max_length,end-start+1)

        return max_length