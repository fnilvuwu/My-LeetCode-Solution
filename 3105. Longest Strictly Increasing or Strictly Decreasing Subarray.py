class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest_strictly_increase = 1
        longest_strictly_decrease = 1
        current_increase = 1
        current_decrease = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_increase += 1
                current_decrease = 1
            elif nums[i] < nums[i-1]:
                current_decrease += 1
                current_increase = 1
            else:
                current_increase = 1
                current_decrease = 1

            longest_strictly_increase = max(longest_strictly_increase, current_increase)
            longest_strictly_decrease = max(longest_strictly_decrease, current_decrease)

        return max(longest_strictly_increase, longest_strictly_decrease)