# Time Complexity - O(N*2)
# Space complexity - O(N)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []    
        for i in range(len(nums)):
            pro = 1
            for j in range(len(nums)):

                if j == i:
                    continue

                pro = pro * nums[j]

            result.append(pro)

        return result


# Time Complexity - O(N)
# Space complexity - O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_pro = [1] * len(nums)
        right_pro = [1] * len(nums)

        pro = 1

        for i in range(1,len(nums)):
            pro = pro * nums[i-1]
            left_pro[i] = pro

        pro = 1

        for i in range(len(nums)-2,-1,-1):
            pro = pro * nums[i+1]
            right_pro[i] = pro

        # print(left_pro,right_pro)

        for i in range(len(left_pro)):
            left_pro[i] *= right_pro[i]

        return left_pro
