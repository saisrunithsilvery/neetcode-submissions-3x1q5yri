class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""

        l = 0
        r = 0

        result_len = float('inf')
        str_point = 0

        t_hash = {}
        s_hash = {}

        # Count characters needed from t
        for index in range(len(t)):
            t_hash[t[index]] = t_hash.get(t[index], 0) + 1

        need = len(t_hash)
        have = 0

        while r < len(s):

            # 1. Add s[r] into the current window
            s_hash[s[r]] = s_hash.get(s[r], 0) + 1

            # 2. If this character now satisfies its required count
            if s[r] in t_hash and s_hash[s[r]] >= t_hash[s[r]]:
                have += 1

            # 3. Shrink window while it is valid
            while have == need:

                # update result
                if result_len > (r - l + 1):
                    str_point = l
                    result_len = r - l + 1

                # remove left character
                s_hash[s[l]] -= 1

                # if removing it makes the window invalid
                if s[l] in t_hash and s_hash[s[l]] < t_hash[s[l]]:
                    have -= 1

                l += 1

            r += 1

        if result_len == float('inf'):
            return ""

        return s[str_point:str_point + result_len]