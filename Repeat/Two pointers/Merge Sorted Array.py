class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1 = nums1[:m]
        if not m:
            nums1.extend(nums2)

        for num in nums2:
            nums1.append(num)
            print(nums1)

        print("nums",nums1)

        nums1.sort()


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if not m:
            nums1 = []
            nums1.extend(nums2)

        nums1_count = 0
        nums2_count = 0

        while nums2_count < n-1:

            if nums1[nums1_count] < nums2[nums2_count]:
                nums1_count += 1
            else:
                nums1.insert(nums1_count+1,nums2[nums2_count])
                nums2_count+=1

                
