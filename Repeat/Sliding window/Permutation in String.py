# Time Complexity - O(N)
# Space complexity - O(N)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        from collections import Counter

        if not s1 or not s2:
            return False

        count_s1 = Counter(s1)
        count_s2 = Counter()

        left,right = 0, 0

        while right < len(s2):
            count_s2[s2[right]] += 1

            while right-left+1 == len(s1):

                if count_s2 == count_s1:
                    return True

                count_s2[s2[left]] -= 1
                left+= 1

            right += 1

        return False
