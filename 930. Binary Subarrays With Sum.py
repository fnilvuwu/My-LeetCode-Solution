class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        sum_dict = {0: 1}
        
        current_sum = 0
        
        for num in nums:
            current_sum += num
            count += sum_dict.get(current_sum - goal, 0)
            sum_dict[current_sum] = sum_dict.get(current_sum, 0) + 1
        
        return count