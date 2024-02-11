class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonal_sum=0
        for col in range(len(mat)):
            diagonal_sum+=mat[col][col]+mat[len(mat)-1-col][col]
        
        return diagonal_sum if len(mat)%2==0 else diagonal_sum-mat[len(mat)//2][len(mat)//2]

