class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in range(len(tokens)):

            if tokens[i] == "+" or tokens[i] == "*" or tokens[i] == "-" or tokens[i] == "/":
                first = stack.pop()
                second = stack.pop()

                result = eval(second+tokens[i]+first)
                stack.append(str(int(result)))
            else:
                stack.append(tokens[i])

        return int(stack[-1])

        