class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        matches = sum(1 for i in range(26) if s1_count[i] == window_count[i])
        if matches == 26:
            return True

        l = 0
        for r in range(n1, n2):
            add_idx = ord(s2[r]) - ord('a')
            if window_count[add_idx] == s1_count[add_idx]:
                matches -= 1
            window_count[add_idx] += 1
            if window_count[add_idx] == s1_count[add_idx]:
                matches += 1

            remove_idx = ord(s2[l]) - ord('a')
            if window_count[remove_idx] == s1_count[remove_idx]:
                matches -= 1
            window_count[remove_idx] -= 1
            if window_count[remove_idx] == s1_count[remove_idx]:
                matches += 1

            l += 1

            if matches == 26:
                return True

        return False