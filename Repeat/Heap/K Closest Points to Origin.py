# Time Complexity - O(NlogN)
# Space complexity - O(N)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        import math
        hash_table = {}
        result = []
        
        for point in points:

            eud_dist = math.sqrt(point[0] ** 2 + point[1]**2)
            if eud_dist in hash_table:
                hash_table[eud_dist].append(point)
            else:
                hash_table[eud_dist] = [point]


        sorted_keys = sorted(hash_table.keys())
        
        result = []
        for key in sorted_keys:
            for point in hash_table[key]:
                if k == 0:
                    return result
                result.append(point)
                k -= 1

        return result

# Time Complexity - O(Nlogk)
# Space complexity - O(N)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        import heapq
        heap = []
        
        for point in points:

            eud_dist = math.sqrt(point[0] ** 2 + point[1]**2)
            eud_dist = -eud_dist  # Negate the distance to use min-heap as max-heap

            if len(heap) == k:
                heapq.heappushpop(heap,(eud_dist,point[0],point[1]))
            else:
                heapq.heappush(heap,(eud_dist,point[0],point[1]))


        return [(x,y) for (distance,x,y) in heap]

