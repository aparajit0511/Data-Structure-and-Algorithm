# Time Complexity - O(N*2)
# Space complexity - O(1)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count_subarray = 0

        for i in range(len(nums)):
            if nums[i] == k:
                count_subarray += 1
            sum = nums[i]
            for j in range(i+1,len(nums)):
                
                sum += nums[j]

                if sum == k:
                    count_subarray += 1

        return count_subarray


# Time Complexity - O(N)
# Space complexity - O(N)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        current_sum = 0
        hash_table = {0:1} #no of times sum 0 appearing

        for i in range(len(nums)):
            current_sum += nums[i]

            if current_sum - k in hash_table:
                result += hash_table[current_sum-k]

            hash_table[current_sum] = hash_table.get(current_sum,0)+1

        return result
