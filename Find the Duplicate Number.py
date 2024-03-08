# Time Complexity - O(N*N)
# Space complexity - O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]

# Time Complexity - O(N)
# Space complexity - O(N)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        findDuplicate = set()

        for i in range(len(nums)):

            if nums[i] in findDuplicate:
                return nums[i]

            findDuplicate.add(nums[i])

# Time Complexity - O(N)
# Space complexity - O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow , fast = 0 , 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow

