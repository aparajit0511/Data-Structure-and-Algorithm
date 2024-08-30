# Time Complexity - O(NlogN)
# Space complexity - O(N) 

class MedianFinder:

    def __init__(self):
        self.nums = []
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        self.nums.sort()
        mid = len(self.nums) // 2
        if len(self.nums) % 2 == 0:  
            return (self.nums[mid] + self.nums[mid-1]) / 2

        return float(self.nums[mid])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Time Complexity - O(logN)
# Space complexity - O(N) 

import heapq

class MedianFinder:

    def __init__(self):
        # to calculate min and max heap
        # small is max heap - smaller elemnts
        # large is min heap - grater elements
        self.small ,self.large = [] , []
        

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,num * -1)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,val * -1)
        elif len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large,val*-1)
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            val1 = self.small[0]
            val2 = self.large[0]
            return (val2 + (val1 * -1)) / 2

        elif len(self.small) > len(self.large):
            return self.small[0] * -1

        elif len(self.large) > len(self.small):
            return self.large[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()