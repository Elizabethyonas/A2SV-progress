# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        remain = k % sum(chalk)
        for i in range(len(chalk)):
            if remain - chalk[i] < 0  or remain == 0:
                return i
            remain -= chalk[i]
