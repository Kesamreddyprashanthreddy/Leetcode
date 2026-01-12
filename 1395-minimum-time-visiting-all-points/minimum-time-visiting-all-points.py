class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1,len(points)):
            x1,y1 = points[i-1]
            x2,y2 = points[i]

            distance_x = abs(x2-x1)
            distance_y = abs(y2-y1)

            time += max(distance_x,distance_y)
            
        return time 
