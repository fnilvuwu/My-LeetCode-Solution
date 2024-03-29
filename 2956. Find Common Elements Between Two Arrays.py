class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_nums1 = 0
        count_nums2 = 0

        for x in nums1:
            if x in nums2:
                count_nums1 += 1

        for x in nums2:
            if x in nums1:
                count_nums2 += 1

        return [count_nums1, count_nums2]