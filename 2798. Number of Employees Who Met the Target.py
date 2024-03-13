class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        sum_target = 0
        for i in hours:
            if i >= target:
                sum_target += 1

        return sum_target