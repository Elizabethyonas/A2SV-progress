class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        checker=defaultdict(int)
        ans=[]
        for num in nums1:
            checker[num]+=1
        for num in nums2:
            if num in checker and checker[num]>0:
                ans.append(num)
                checker[num]-=1
        return ans