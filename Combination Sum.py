# Time Complexity - O(N*2^N)  need to optimize this
# Space complexity - O(N*2^N)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []

        return self.findCombination(candidates,[],result,target,0)


    def findCombination(self,candidates,combinations,result,target,start_index):

        if sum(combinations) > target:
            return result

        if sum(combinations) == target:
            result.append(list(combinations))
            return result

        for i in range(start_index,len(candidates)):
            combinations.append(candidates[i])
            result = self.findCombination(candidates,combinations,result,target,i)
            combinations.pop()

        return result