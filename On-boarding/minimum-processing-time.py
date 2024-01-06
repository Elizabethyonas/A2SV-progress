class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        latestTime=0
        for i in range(0,len(tasks),4):
            processorIndex=i//4
            FinishTime=processorTime[processorIndex]+tasks[i]
            latestTime=max(FinishTime,latestTime)
        return latestTime