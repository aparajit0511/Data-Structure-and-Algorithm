class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        return self.backtrack(nums,[],[])

    def backtrack(self,nums,path,result):

        if len(path) == len(nums):
            result.append(path[:])
            return result

        for i in range(len(nums)):

            if nums[i] in path:
                continue

            path.append(nums[i])

            result = self.backtrack(nums,path,result)
            path.pop()

        return result




class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        return self.backtrack(nums,[],0)

    def backtrack(self,nums,result,start):

        if start == len(nums):
            result.append(nums[:])
            return result


        for i in range(start,len(nums)):

            nums[i] , nums[start] = nums[start] , nums[i]

            result = self.backtrack(nums,result,start+1)

            nums[i] , nums[start] = nums[start] , nums[i]

        return result