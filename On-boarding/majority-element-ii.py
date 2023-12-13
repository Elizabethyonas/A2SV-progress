class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        rep=len(nums)/3
        frequency_dict={}
        ans=[]
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num]+=1
            else:
                frequency_dict[num] = 1
            if frequency_dict[num]>rep and num not in ans:
                ans.append(num)
            else:
                continue
        return ans
