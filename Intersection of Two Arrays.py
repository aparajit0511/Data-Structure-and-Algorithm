# Time Complexity: O(len(nums1)) , Space Complexity: O(min(len(nums1), len(nums2)))

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums2 = set(nums2)

        result = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                result.append(nums1[i])

        return list(set(result))


# Time Complexity: O(len(nums1) + len(nums2)) , Space Complexity: O(len(nums1) + len(nums2))
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1 =set(nums1)
        nums2 = set(nums2)

        result = []

        if len(nums1) <= len(nums2):
            result = self.setIntersection(nums1,nums2,result)
        else:
            result = self.setIntersection(nums2,nums1,result)

        return result

    def setIntersection(self,numsA,numsB,result):
        for i in numsA:
            if i in numsB:
                result.append(i)

        return result