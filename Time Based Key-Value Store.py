# Time Complexity - O(LogN)
# Space complexity - O(1)

from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.hashMap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashMap:
            
            values = self.hashMap[key]
            start,end = 0, len(values)-1

            while start <= end:

                mid = (start + end) // 2
                
                if values[mid][0] == timestamp:
                    return values[mid][1]
                elif values[mid][0] < timestamp:
                    start = mid + 1
                else:
                    end = mid - 1

            return values[end][1] if end >= 0 else ""
        else:
            return ""
         


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)