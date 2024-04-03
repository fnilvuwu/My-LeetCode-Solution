class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1
            
        for i in nums:
            if freq[i] > 2:
                return False

        return True