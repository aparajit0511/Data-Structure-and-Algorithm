# Time Complexity - O(max_banana * n)
# Space complexity - O(1) 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_banana = max(piles)
        k = 1
        result = max_banana

        while k <= max_banana:
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / k)

            # print(hours)

            if hours <= h:
                result = min(result,k)

            k+=1

        return result


# Time Complexity - O(n * log(max_banana))
# Space complexity - O(1) 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        start , end = 1 , max(piles)
        result = end

        while start <= end:
            hours = 0
            mid = (start + end) // 2

            for pile in piles:
                hours += math.ceil(float(pile) / mid)

            if hours <= h:
                result = min(result,mid)
                end = mid - 1
            else:
                start = mid + 1

        return result