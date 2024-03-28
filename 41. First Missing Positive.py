class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positive_numbers = set(filter(lambda x: x > 0, nums))
        i = 1
        while True:
            if i not in positive_numbers:
                return i
            i += 1