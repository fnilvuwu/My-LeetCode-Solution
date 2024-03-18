class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points = sorted(points)
        
        arrows = 1
        prev_end = points[0][1]
        
        for balloon in points[1:]:
            if balloon[0] > prev_end:
                arrows += 1
                prev_end = balloon[1]
            else:
                prev_end = min(prev_end, balloon[1])  
                
        return arrows