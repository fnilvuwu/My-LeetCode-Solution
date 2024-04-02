class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr, size = sorted(arr), len(arr)

        res = [arr[i + 1] - arr[i] for i in range(size - 1)]

        min_diff = min(res)
        arr_smallest = [[arr[i], arr[i + 1]] for i in range(size - 1) if arr[i + 1] - arr[i] == min_diff]
            
        return arr_smallest