class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds=0
        for i in range(1,len(points)):
            x1=points[i-1][0]
            y1=points[i-1][1]
            x2=points[i][0]
            y2=points[i][1]
            seconds+=max(abs(x1-x2), abs(y1-y2))
        return seconds
