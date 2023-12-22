class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result=[]
        for lst in zip(*matrix):
            result.append(list(lst))

        return result