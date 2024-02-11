class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Count the characters in t
        target_count = Counter(t)

        # Initialize variables for sliding window
        left, right = 0, 0
        required_chars = len(target_count)
        formed_chars = 0
        window_count = Counter()
        min_len = float('inf')
        result = ""

        while right < len(s):
            # Expand the window
            window_count[s[right]] += 1
            if window_count[s[right]] == target_count[s[right]]:
                formed_chars += 1

            # Contract the window
            while formed_chars == required_chars:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                window_count[s[left]] -= 1
                if window_count[s[left]] < target_count[s[left]]:
                    formed_chars -= 1

                left += 1

            right += 1

        return result  