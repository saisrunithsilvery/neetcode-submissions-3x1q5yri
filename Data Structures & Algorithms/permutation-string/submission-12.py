class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i, char in enumerate(s1):
            s1_count[ord(char) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        l = 0
        r = len(s1)

        while r < len(s2):

            if s1_count == s2_count:
                return True

            # remove left character
            s2_count[ord(s2[l]) - ord('a')] -= 1
            l += 1

            # add right character
            s2_count[ord(s2[r]) - ord('a')] += 1
            r += 1

        # IMPORTANT: check the final window
        return s1_count == s2_count