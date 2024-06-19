# Time Complexity - O(N*N!)
# Space complexity - O(N*N!)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        return self.checkPermutation(nums,[],[])

    def checkPermutation(self,nums,result,path):

        if len(path) == len(nums):
            result.append(path[:])
            return result

        for i in range(len(nums)):
            if nums[i] in path:
                continue

            path.append(nums[i])
            result = self.checkPermutation(nums,result,path)
            path.pop()

        return result


# Time Complexity - O(N!)
# Space complexity - O(N!)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        return self.checkPermutation(nums,0,[])

    def checkPermutation(self,nums,start,result):

        if start == len(nums):
            result.append(nums[:])
            return result

        for i in range(start,len(nums)):
            
            # Swap the current element with the start element
            nums[i] , nums[start] = nums[start],nums[i]

            result = self.checkPermutation(nums,start+1,result)

             # Swap back to backtrack
            nums[i] , nums[start] = nums[start],nums[i]

        return result

