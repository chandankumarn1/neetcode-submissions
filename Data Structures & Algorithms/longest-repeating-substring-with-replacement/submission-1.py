class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxFreq = 0
        maxLength = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            maxFreq = max(maxFreq, count[s[right]])

            windowLength = right - left + 1
            replacements = windowLength - maxFreq

            while replacements > k:
                count[s[left]] -= 1
                left += 1

                windowLength = right - left + 1
                replacements = windowLength - maxFreq

            maxLength = max(maxLength, right - left + 1)

        return maxLength