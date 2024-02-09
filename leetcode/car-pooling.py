class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix=[0]*1001
        for i in range(len(trips)):
            From=trips[i][1]
            to=trips[i][2]
            people=trips[i][0]
            prefix[From]+=people
            prefix[to]-=people
        for j in range(len(prefix)):
            prefix[j]+=prefix[j-1] 
            if prefix[j]>capacity:
                return False

        return True

        
