# Time Complexity - O(N log N)
# Space complexity - O(1) 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        while len(stones) > 1:

            stones.sort()
            # print(stones)
            stone1 = stones[-1]
            stones.pop()
            stone2 = stones[-1]
            stones.pop()
            result = abs(stone1 - stone2)
            if result > 0:
                stones.append(result)

        return 0 if len(stones) == 0 else stones[0]


# Time Complexity - O(N log N) with heapsort
# Space complexity - O(1)

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)  # log(N)
            stone2 = -heapq.heappop(stones)  # log(N)

            result = abs(stone1 - stone2)
            if result > 0:
                heapq.heappush(stones,-result)

        return 0 if len(stones) == 0 else abs(stones[0])