# Time Complexity - O(N^2)
# Space complexity - O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_Profit = 0

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):

                max_Profit = max(max_Profit,prices[j]-prices[i])

        return max_Profit


# Time Complexity - O(N)
# Space complexity - O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start , end = 0, 0
        max_Profit = 0

        while end < len(prices):

            if start != end and prices[end] < prices[start]:
                start = end

            if start != end and prices[end] > prices[start]:
                max_Profit = max(max_Profit,prices[end]-prices[start])

            end += 1

        return max_Profit
