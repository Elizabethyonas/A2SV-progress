class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.remove(salary[0])
        salary.remove(salary[len(salary)-1])
        sum = 0
        for i in range(len(salary)):
            sum += salary[i]
            i += 1
        return float(sum/(len(salary)))