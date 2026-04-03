class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}  # dictionary to store character counts

        # Count characters in s
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Subtract counts using characters in t
        for ch in t:
            if ch not in count:   # char never appeared in s
                return False
            count[ch] -= 1
            if count[ch] < 0:    # t has more of this char than s
                return False

        # If all counts are zero, it's an anagram
        return True             



        