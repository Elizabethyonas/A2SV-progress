class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        arr=[]
        for num in nums:
            if num>0:
                pos.append(num)
            else:
                neg.append(num)
        for p,n in zip(pos,neg):
            arr.append(p)
            arr.append(n)
        return arr