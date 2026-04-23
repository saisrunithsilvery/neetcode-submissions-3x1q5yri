class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        result = []

        x = "".join(str(d) for d in digits)

        x = int(x)

        x +=1

        for i in str(x):

            result.append(int(i))

        return result    





        