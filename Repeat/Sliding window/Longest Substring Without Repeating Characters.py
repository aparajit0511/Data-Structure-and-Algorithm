# Time Complexity - O(N^2)
# Space complexity - O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_substring = 0
        s = list(s)

        for i in range(len(s)):
            temp = set()
            for j in range(i,len(s)):

                if s[j] not in temp:
                    temp.add(s[j])
                    max_substring = max(max_substring,j-i+1)
                else:
                    break

        return max_substring

# Time Complexity - O(N)
# Space complexity - O(N)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_substring = 0
        temp = set()

        s = list(s)
        start , end = 0 , 0

        while end < len(s):

            while s[end] in temp:
                max_substring = max(max_substring,end-start)
                if s[start] in temp:
                    temp.remove(s[start])
                    start += 1
            temp.add(s[end])
            end += 1

        return max(max_substring,len(temp))

