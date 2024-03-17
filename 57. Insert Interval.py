class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_array_interval = []
        for i in intervals:
            if newInterval[0] in [i for i in range(i[0], i[1]+1)]:
                if i[0] > newInterval[0]:
                    i[0] = newInterval[0]
                if i[1] < newInterval[1]:
                    i[1] = newInterval[1]
            else:
                new_array_interval.append(newInterval)
            new_array_interval.append(i)

        def merge_intervals(intervals):
            if not intervals:
                return [newInterval]

            intervals.sort(key=lambda x: x[0])  # Sort intervals based on start points
            merged = [intervals[0]]

            for interval in intervals[1:]:
                if interval[0] <= merged[-1][1]:  # If overlapping
                    merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
                else:
                    merged.append(interval)

            return merged

        return merge_intervals(new_array_interval)
                    