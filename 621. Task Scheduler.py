from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = [0] * 26
        # AAABBB 2
        for task in tasks:
            # since the array starts from 0 but ascii alphabet starts from 65
            task_counts[ord(task) - ord('A')] += 1

        # task_counts = [3][3][0][0]...[0]
        # this will return 3
        max_count = max(task_counts)
        # this will return 2
        max_count_tasks = task_counts.count(max_count)
        
        # (3 - 1) * (2 + 1) + 2 = 8
        min_intervals = (max_count - 1) * (n + 1) + max_count_tasks
        
        # if the minimum intervals is less than the length of the tasks, return the length of the tasks
        return max(min_intervals, len(tasks))