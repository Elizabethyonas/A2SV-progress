class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count=defaultdict(int)
        ans=[]
        last=[]    
        for num1 in arr1:
            count[num1]+=1
            if num1 not in arr2:
                last.append(num1)
        for num2 in arr2:
            if num2 in count:
                ans.extend([num2]*count[num2])
        last.sort()
        return ans+last