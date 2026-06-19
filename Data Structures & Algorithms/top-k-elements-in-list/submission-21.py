class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        result = [None]*(len(nums))
        for i in nums:
            dict1[i] = dict1.get(i, 0) + 1
        for key, value in dict1.items():
            result[value] = key
        result1 = []    
        for i in range(len(result)-1, -1):
            if count == k:
                return result1
            if result[i]!= None:
                result1.append(key)
                count +=1
        return result1        




