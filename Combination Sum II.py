# Time Complexity - O(2^N)
# Space complexity - O(N*2^N)

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        return self.findCombination(candidates,[],[],target,0)

    def findCombination(self,candidates,combinations,result,target,total):

        if total > target:
            return result

        if total == target:
            result.append(list(combinations[:]))
            return result

        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            combinations.append(candidates[i])
            result = self.findCombination(candidates[i+1:],combinations,result,target,total+candidates[i])
            combinations.pop()

        return result