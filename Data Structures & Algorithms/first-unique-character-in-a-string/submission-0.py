class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Count frequencies
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # Step 2: Find first char with freq 1
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        
        return -1