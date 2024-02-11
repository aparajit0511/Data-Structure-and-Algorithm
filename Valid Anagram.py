## Time complexity - O(NMlogNM) Space Complexity - O(N+M)
## This is because the sorted strings are stored in memory, and the space required is proportional to the length of the strings.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        if s == t:
            return True

        return False

## Time complexity - O(N+M) Space Complexity - O(N+M)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        for i in s:
            if i not in hash_s:
                hash_s[i] = 1
            else:
                hash_s[i] += 1

        for i in t:
            if i not in hash_t:
                hash_t[i] = 1
            else:
                hash_t[i] += 1

        if hash_t == hash_s:
            return True

        return False