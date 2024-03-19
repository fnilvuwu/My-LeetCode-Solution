from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = [0] * 26
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1
        
        max_count = max(task_counts)
        max_count_tasks = task_counts.count(max_count)
        
        min_intervals = (max_count - 1) * (n + 1) + max_count_tasks
        
        return max(min_intervals, len(tasks))