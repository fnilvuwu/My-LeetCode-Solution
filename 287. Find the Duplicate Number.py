class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq_map = {}
        
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1
        
        for num, freq in freq_map.items():
            if freq > 1:
                return num