class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points)
        x_coordinates = [point[0] for point in points]
        max_diff = max([y - x for x, y in zip(x_coordinates, x_coordinates[1:])], default=0)
        return max_diff