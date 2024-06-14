# Time Complexity - O(N log N)
# Space complexity - O(1)

class Solution:
    def kClosest(self, P, k):
        return sorted(P, key=lambda p: p[0]**2 + p[1]**2)[:k]

# Time Complexity - O(N log K)
# Space complexity - O(N)

class Solution:
    def kClosest(self, P, k):

        heap = []

        for (x,y) in P:
            distance = x * x+ y * y
            distance = -distance


            if len(heap) == k:
                heapq.heappushpop(heap,(distance,x,y))
            else:
                heapq.heappush(heap,(distance,x,y))

        return [(x,y) for (distance,x,y) in heap]