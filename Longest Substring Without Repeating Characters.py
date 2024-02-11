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

