class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []
        n = len(A)
        while A:
            smallest = A.index(min(A))
            res.append(smallest + 1)
            res.append(len(A))
            A = list(reversed(A[:smallest + 1])) + A[smallest + 1:]
            A.reverse()
            del A[-1]
        res.append(n)
        return res
        