class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left, longest, max_count = 0, 0, 0
        counts = {'T': 0, 'F': 0}

        for right in range(len(answerKey)):
            counts[answerKey[right]] += 1
            max_count = max(max_count, counts[answerKey[right]])

            while (right - left + 1) - max_count > k:
                counts[answerKey[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest