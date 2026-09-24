class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countT = {}
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        window = {}

        have = 0
        need = len(countT)

        left = 0
        minLength = float("inf")
        minLeft = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # Character has reached the required frequency
            if ch in countT and window[ch] == countT[ch]:
                have += 1

            # Try to shrink the window
            while have == need:
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    minLeft = left

                leftChar = s[left]
                window[leftChar] -= 1

                if leftChar in countT and window[leftChar] < countT[leftChar]:
                    have -= 1

                left += 1

        if minLength == float("inf"):
            return ""

        return s[minLeft:minLeft + minLength]