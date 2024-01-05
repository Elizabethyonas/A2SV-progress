class Solution:
    def smallestNumber(self, num: int) -> int:
        nums=[]
        zeros=0
        st=str(num)
        if num==0:
            return 0
        elif num<0:
            for i in range(1,len(st)):
                if st[i]=='0':
                    zeros+=1
                else:
                    nums.append(st[i])
            nums.sort(reverse=True)
            finalNum=''.join(nums)
            return int('-'+finalNum+'0'*zeros)
        elif num>0:
            for i in range(len(st)):
                if st[i]=='0':
                    zeros+=1
                    
                else:
                    nums.append(st[i])
            nums.sort()
            finalNum=''.join(nums)
            return int(finalNum[0]+'0'*zeros+finalNum[1:])

