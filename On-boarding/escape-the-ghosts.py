class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        for i in range(len(ghosts)):
            x1=ghosts[i][0]
            y1=ghosts[i][1]
            x2=target[0]
            y2=target[1]
            my_step=abs(x2)+abs(y2)
            ghosts_step=abs(x2-x1)+abs(y2-y1)
            if my_step>=ghosts_step:
                return False
            

        return True