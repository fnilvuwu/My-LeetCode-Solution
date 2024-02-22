class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            y = target - nums[i]
            if y in nums and i != nums.index(y):
                if i > nums.index(y):
                    return [nums.index(y), i]
                else:
                    return [i, nums.index(y)]