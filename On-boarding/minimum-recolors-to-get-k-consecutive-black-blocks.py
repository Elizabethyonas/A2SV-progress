class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_op=k
        for i in range(len(blocks)):
            count=blocks[i:i+k].count("B")
            if count>k:
                return 0
            min_op=min(min_op,k-count)
        return min_op