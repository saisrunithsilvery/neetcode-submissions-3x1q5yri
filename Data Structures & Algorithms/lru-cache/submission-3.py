class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node()    # LRU dummy
        self.right = Node()   # MRU dummy
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        x = node.next         # you had this ✅
        y = node.prev         # you had this ✅
        y.next = x            # you had this ✅
        x.prev = y            # you missed this ❌

    def add(self, node):
        # insert before right dummy
        x = self.right.prev   # you had this ✅
        x.next = node         # you missed this ❌
        node.prev = x         # you missed this ❌
        node.next = self.right # you missed this ❌
        self.right.prev = node # you had this ✅

    def get(self, key: int) -> int:
        if key in self.cache:          # self. ❌ missing
            node = self.cache[key]
            self.remove(node)          # self. ❌ missing
            self.add(node)             # self. ❌ missing
            return node.val            # return ❌ missing
        return -1                      # return -1 ❌ missing

    def put(self, key: int, value: int) -> None:
        if key in self.cache:          # update existing
            self.cache[key].val = value
            node = self.cache[key]
            self.remove(node)
            self.add(node)
        else:                          # new key
            node = Node(key, value)    # ❌ you never created new node
            self.cache[key] = node
            self.add(node)
            if len(self.cache) > self.cap:   # evict LRU
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]      # ❌ delete from cache too