## Time Complexity - O(N*2)
## Space Complexity - O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        visited = set()

        for i in range(len(s)):
            visited.add(s[i])
            for j in range(i+1,len(s)):
                if s[j] in visited:
                    break

            max_length = max(max_length,j-i+1)

        return max_length

## Time Complexity - O(N)
## Space Complexity - O(N)
class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:

        max_length = 0
        visited = set()

        start,end = 0,0

        while end < len(nums):

            while nums[end] in visited:
                max_length = max(max_length,end-start)
                if nums[start] in visited:
                    visited.remove(nums[start])
                    start += 1

            visited.add(nums[end])
            end += 1

        return max(max_length,len(visited))
        