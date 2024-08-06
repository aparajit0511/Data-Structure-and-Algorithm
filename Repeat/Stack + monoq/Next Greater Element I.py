# Time Complexity: O(M*N) and Space Complexity: O(N)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []

        for i in range(len(nums1)):

            index = nums2.index(nums1[i])
            found = 0
            # print(nums2[index],index)

            for j in range(index+1,len(nums2)):
               
                if nums2[j] > nums2[index]:
                    result.append(nums2[j])
                    found = 1
                    break

            if found == 0:
                result.append(-1)

        return result

# Time Complexity: O(M+N) and Space Complexity: O(N)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        hash_table = {}
        result = []

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