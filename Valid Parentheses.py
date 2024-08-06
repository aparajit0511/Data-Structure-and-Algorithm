# Time Complexity: O(N) and Space Complexity: O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s = list(s)
        print(len(s))

        if len(s) % 2 == 1:
            return False

        # stack.append(s[0])

        for i in range(len(s)):
            print("i->",s[i])

            if stack:
                print("stack",stack[-1])

            if stack and stack[-1] == "(" and s[i] == ")":
                stack.pop()
            elif stack and  stack[-1] == "[" and s[i] == "]":
                stack.pop()
            elif stack and stack[-1] == "{" and s[i] == "}":
                stack.pop()

            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])

        print(stack)


        hash_table = {"{":0,"}":0,"[":0,"]":0,"(":0,")":0}

        for i in s:
            hash_table[i] += 1

        if hash_table["("] != hash_table[")"]:
            return False
        elif hash_table["["] != hash_table["]"]:
            return False
        elif hash_table["{"] != hash_table["}"]:
            return False



        return True if len(stack) == 0 else False