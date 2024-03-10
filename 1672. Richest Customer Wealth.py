class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for account in accounts:
            sum_acc = sum(account)
            if sum_acc > max_sum:
                max_sum = sum_acc
        return max_sum
