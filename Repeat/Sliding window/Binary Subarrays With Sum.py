# Time Complexity: O(N*2) and Space Complexity: O(1)
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        count_subArrays = 0

        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]

                if sum == goal:
                    print(j,i)
                    count_subArrays += 1

        return count_subArrays


# Time Complexity: O(N) and Space Complexity: O(N)
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        count_subArrays = 0
        hash_table = {0:1}
        current_sum = 0

        for i in range(len(nums)):

            current_sum += nums[i]

            if current_sum - goal in hash_table:
                count_subArrays += hash_table[current_sum-goal]

            hash_table[current_sum] = hash_table.get(current_sum,0)+1

        return count_subArrays