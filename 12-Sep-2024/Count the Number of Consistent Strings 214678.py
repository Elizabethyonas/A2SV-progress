# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for chr in words:
            flag = True
            for ch in chr:
                if ch not in allowed:
                    flag = False
                    break
            if flag:
                count += 1
        return count

            