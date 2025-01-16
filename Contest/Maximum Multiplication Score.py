class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:

        return self.maxFind(a,b,float("-inf"),0,0)


    def maxFind(self,a,b,maxValue,value,start):

        if start == len(b)-1:
            maxValue = max(value,maxValue)
            return maxValue

        i = 0
        while i < len(a) and start < len(a):
            value += self.maxFind()
            i += 1
            
