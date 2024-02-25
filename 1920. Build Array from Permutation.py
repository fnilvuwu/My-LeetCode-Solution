class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp_nums = nums
        return [temp_nums[x] for x in nums]
        