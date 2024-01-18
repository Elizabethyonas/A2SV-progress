class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left=0
        right=k
        minop=float('inf')
        while right<=len(blocks):
            cnt=blocks[left:right].count("W")
            minop=min(minop,cnt)
            left+=1
            right+=1
        return minop if minop!=float('inf') else 0
