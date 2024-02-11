# Non-optimized/brute force will be O(N*4)

#  Time Complexity: O(NlogN + N*3) and Space Complexity: O(1)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        result = set()

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                left = j+1
                right = len(nums)-1

                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        result.add((nums[i] , nums[j] , nums[left] , nums[right]))
                        left+=1
                        right-=1
                    elif sum < target:
                        left +=1
                    else:
                        right -=1
        unique = []

        for i in list(result):
            unique.append(list(i))

        return unique
