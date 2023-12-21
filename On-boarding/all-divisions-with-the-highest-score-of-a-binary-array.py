class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count = defaultdict(list)
        count[nums.count(0)].append(len(nums))
        count[nums.count(1)].append(0)
        one = nums.count(1)
        zero=0
        

        for i in range(1,len(nums)):     
    
            if nums[i-1]==0:
                zero+=1
            else:
                one-=1
            


            
          
            
            count[one + zero ].append(i)

        return count[max(count)]