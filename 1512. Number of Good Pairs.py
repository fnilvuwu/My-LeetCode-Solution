from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pair = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    good_pair += 1

        return good_pair
