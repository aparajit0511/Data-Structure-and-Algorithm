# Time Complexity: O(NlogN + N*3) and Space Complexity: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        unique = []
        nums.sort()

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):

                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add((nums[i],nums[j],nums[k]))
                        
        for i in list(result):
            unique.append(list(i))
            

        return unique

# Time Complexity: O(NlogN + N*2) and Space Complexity: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        unique = []
        nums.sort()

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]

                if sum < 0:
                    left +=1
                elif sum > 0:
                    right -=1
                elif sum == 0:
                    result.add((nums[i],nums[left],nums[right]))
                    left +=1
                    right-=1

        for i in list(result):
            unique.append(list(i))
            

        return unique
