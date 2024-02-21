class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        check = defaultdict(int)
        count = 0
        for num in answers:
            if num == 0:
                count += 1
            elif check[num] == 0:
                check[num] += 1
                count += num + 1
            elif check[num] == num+1:
                check[num] = 0
                count += num + 1
                check[num] += 1
            else:
                check[num] += 1
        return count
