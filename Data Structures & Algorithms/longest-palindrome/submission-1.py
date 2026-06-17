class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        count = 0

        for i in s:
            hashmap[i] = hashmap.get(i, 0)+1


        for i in hashmap.values():

            if i%2 == 0:
                count += i
            else:
                if i-1 != 0:
                    count += i-1
        return count + 1           

