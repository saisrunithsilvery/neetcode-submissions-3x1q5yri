class MyHashSet:

    def __init__(self):
        self.set1 = [False] * (10**6 + 1)
        

    def add(self, key: int) -> None:

        self.set1[key] = True
        

    def remove(self, key: int) -> None:
        self.set1[key] = False
        

    def contains(self, key: int) -> bool:
        return self.set1[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)