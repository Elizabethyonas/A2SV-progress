class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        path1=0
        path2=0
        total_distance=0
        for i in range(len(distance)):
            total_distance+=distance[i]
        #for clockwise
        for i in range(min(start, destination), max(start, destination)):
            path1+=distance[i]
        #for counter-clockwise
        path2=total_distance-path1

        return min(path1,path2)

        