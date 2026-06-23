class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # prefix[k] = number of valid words in words[0..k-1]
        prefix = [0] * (len(words) + 1)
        for i, word in enumerate(words):
            prefix[i + 1] = prefix[i] + (word[0] in vowels and word[-1] in vowels)

        return [prefix[j + 1] - prefix[i] for i, j in queries]