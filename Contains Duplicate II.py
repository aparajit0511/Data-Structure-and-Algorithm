# Time Complexity: O(n * 2) and Space Complexity: O(1)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True

        return False

# Time Complexity: O(n * k) and Space Complexity: O(n)
from collections import defaultdict 
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = defaultdict(list)

        for i in range(len(nums)):
            if nums[i] in hash_table:
                # print(hash_table)
                for j in hash_table[nums[i]]:
                    if abs(j - i) <= k:
                        return True
                hash_table[nums[i]].append(i)
            else:
                hash_table[nums[i]].append(i)

        return False


# Chatgpt solution
# Time Complexity: O(n) and Space Complexity: O(min(n,k))
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = {}

        for index,element in enumerate(nums):
            if element in hash_table and abs(index - hash_table[element]) <= k:
                return True
            hash_table[element] = index

        return False