# Time Complexity - O(N*N!)
# Space complexity - O(N*N!)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        return self.findPermutations(nums,[],[])


    def findPermutations(self,nums,result,path):
        if len(path) == len(nums):
            result.append(path[:])
            return result

        for i in range(len(nums)):
            # to remove repetition
            if nums[i] in path:
                continue

            path.append(nums[i])
            result = self.findPermutations(nums,result,path)
            path.pop()

        return result


# Time Complexity - O(N!)
# Space complexity - O(N!)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        return self.findPermutations(nums,[],0)


    def findPermutations(self,nums,result,start):

        if start == len(nums):
            result.append(nums[:])
            return result

        for i in range(start,len(nums)):

            nums[i],nums[start] = nums[start],nums[i]
            result = self.findPermutations(nums,result,start+1)
            nums[i],nums[start] = nums[start],nums[i]

        return result



