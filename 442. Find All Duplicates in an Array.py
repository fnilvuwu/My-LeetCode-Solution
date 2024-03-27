class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        n = len(nums)
        for x in nums:
            x = abs(x)
            if nums[x-1]<0:
                duplicates.append(x)
            nums[x-1] *= -1
        return duplicates