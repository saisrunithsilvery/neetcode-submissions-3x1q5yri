class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowels = {'a','e','i','o','u'}

        output =[False]*(len(words))
        result = []

        for i, word in enumerate(words):

            if word[0] in vowels and word[-1] in vowels:
                output[i] = True

        for i , j in queries:
            count = 0

            while i <=j:
                if output[i]:
                    count +=1
                i +=1
            result.append(count)
        return result    

                    



        