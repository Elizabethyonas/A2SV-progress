class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans=[]
        left=0
        right=0
        if firstList==[] or secondList==[]:
            return []
        while left<len(firstList) and right<len(secondList):
            first=max(firstList[left][0],secondList[right][0])
            second=min(firstList[left][1],secondList[right][1])
            if first<=second:
                ans.append([first,second])
            if firstList[left][1]<secondList[right][1]:
                left+=1
            else:
                right+=1
        return ans

