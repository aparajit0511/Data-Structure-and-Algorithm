# Time Complexity - O(N^2)
# Space Complexity - O(N)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = [-1] * len(nums1)

        for i in range(len(nums1)):

            flag = 0

            for j in range(len(nums2)):

                if nums1[i] == nums2[j]:
                    flag = 1

                if flag == 1 and nums1[i] < nums2[j]:
                    result[i] = nums2[j]
                    break

        return result


# Time Complexity - O(N)
# Space Complexity - O(N)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []

        stack = []
        hash_table = {}

        for i in range(len(nums2)):

            while stack and stack[-1] < nums2[i]:
                item = stack.pop()
                hash_table[item] = nums2[i]

            stack.append(nums2[i])


        for i in range(len(nums1)):

            if nums1[i] in hash_table:
                result.append(hash_table[nums1[i]])
            else:
                result.append(-1)

        return result