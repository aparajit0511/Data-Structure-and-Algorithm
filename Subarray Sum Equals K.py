class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == k:
                count += 1
            sum = nums[i]
            for j in range(i+1,len(nums)):
                sum += nums[j]
                if sum == k:
                    count +=1

        return count

# will work on only +ive numbers
from collections import deque
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        queue = deque()
        sum , count = 0 , 0

        for i in range(len(nums)):
            sum += nums[i]
            queue.append(i)

            while sum > k:
                item = queue.popleft()
                sum = sum - nums[item]

            if sum == k and queue:
                count += 1

        return count

#Time and Space - O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        currentSum = 0
        hash_table = {0:1}  #no of times sum 0 appearing

        for i in range(len(nums)):
            currentSum += nums[i]

            if currentSum - k in hash_table:
                result += hash_table[currentSum-k]

            hash_table[currentSum] = hash_table.get(currentSum,0) + 1

        return result

        