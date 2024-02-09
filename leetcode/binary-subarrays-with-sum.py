class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix_sum = 0
        total_count = 0

        for num in nums:
            prefix_sum += num
            complement = prefix_sum - goal
            total_count += count[complement]
            count[prefix_sum] += 1

        return total_count
        # arr=0
        # left=0
        # sum=0
        # for right in range(len(nums)):
        #     sum+=nums[right]
        #     if sum==goal:
        #         print(left,right)
        #         arr+=1
        #     while sum>goal:
        #         sum-=nums[left]
        #         left+=1
        #         if sum==goal:
        #             arr+=1
        #             print(left,right)
        #         while sum==goal and left<=right:
        #             sum-=nums[left]
        #             left+=1
        #             if sum==goal:
        #                 arr+=1
        #                 print(left,right)
            
        # return arr
                          
