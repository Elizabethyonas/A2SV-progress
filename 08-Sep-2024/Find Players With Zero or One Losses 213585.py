# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict1=defaultdict(int)
        loses0=[]
        loses1=[]
        for match in matches:
            dict1[match[0]]=0
        for match in matches:
            dict1[match[1]]+=1
        for val in dict1:
            if dict1[val]==0:
                loses0.append(val)
            if dict1[val]==1:
                loses1.append(val)
        loses0.sort()
        loses1.sort()
        ans= [loses0,loses1]
        return ans