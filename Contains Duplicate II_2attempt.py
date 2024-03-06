# Time Complexity - O(N*N)
#Space complexity - O(1)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True

        return False


# Time Complexity - O(N)
#Space complexity - O(N)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hash_table = {}

        for i in range(len(nums)):

            if nums[i] not in hash_table:
                hash_table[nums[i]] = i;
            else:
                if abs(hash_table[nums[i]] - i) <= k:
                    return True
                else:
                    hash_table[nums[i]] = i

        return False

# A better code
# Time Complexity - O(N)
#Space complexity - O(N)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hash_table = {}

        for i in range(len(nums)):

            if nums[i] in hash_table and abs(hash_table[nums[i]]-i) <= k:
                return True
            
            hash_table[nums[i]] = i

        return False