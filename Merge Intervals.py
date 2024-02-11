class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        result = []
        visited =set()

        for i in range(len(intervals)-1):
            pair1 = intervals[i]

            for j in range(i,i+1):
                pair2 = intervals[j]
                if pair1[1] >= pair2[0] and pair1[1] >= pair2[1]:
                    visited.add([pair1])
                    continue
                elif pair1[1] >= pair2[0] and pair1[1] <= pair2[1]:
                    visited.add([pair[1],pair2[1]])
                elif pair1[1] < pair2[0]:
                    visited.add([pair2])
                    continue

        return result.append(list(visited))