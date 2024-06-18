# Time Complexity - O(2^N)
# Space complexity - O(N*2^N)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        total_subsets = 2 ** len(nums)

        return self.findSubsets(nums,[],total_subsets,[])

    def findSubsets(self,nums,result,total_subsets,subset):
        if len(result) == total_subsets:
            return result
        else:
            result.append(list(subset))


        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            result = self.findSubsets(nums[i+1:],result,total_subsets,subset)
            subset.pop()

        return result