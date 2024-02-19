class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        reference=defaultdict(lambda : -1)
        stack=[]
        for num in nums2:
            while stack and stack[-1] < num:
                reference[stack[-1]] = num
                stack.pop()
            stack.append(num)

        return [reference[num1] for num1 in nums1]
