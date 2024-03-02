class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = {}
        ans = []
        for i in range(len(s)):
            if s[i] in intervals:
                intervals[s[i]][1] = i
            else:
                intervals[s[i]] = [i, i]
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, intervals[s[i]][1])
            if i == end:
                ans.append(end - start + 1)
                start = end + 1
        return ans
