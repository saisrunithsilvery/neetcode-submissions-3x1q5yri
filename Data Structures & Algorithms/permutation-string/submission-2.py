class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1count = [0] * 26
        s2count = [0] * 26
        matches = 0
        
        # Build initial window
        for i in range(len(s1)):
            index = ord(s1[i]) - ord("a")
            s1count[index] += 1
            index1 = ord(s2[i]) - ord("a")
            s2count[index1] += 1

        # Count initial matches
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1

        # Check initial window
        if matches == 26:
            return True

        # Slide the window
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            # Remove left character
            left_index = ord(s2[i - len(s1)]) - ord('a')
            if s2count[left_index] == s1count[left_index]:
                matches -= 1
            s2count[left_index] -= 1
            if s2count[left_index] == s1count[left_index]:
                matches += 1
            
            # Add right character
            right_index = ord(s2[i]) - ord('a')
            if s2count[right_index] == s1count[right_index]:
                matches -= 1
            s2count[right_index] += 1
            if s2count[right_index] == s1count[right_index]:
                matches += 1
            
            # Check if we found a match
            if matches == 26:
                return True
                
        return False