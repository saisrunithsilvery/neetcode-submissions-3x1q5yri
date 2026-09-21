class ListNode:
    def __init__(self, val = None):
        self.value = val
        self.next = None
        self.prev = None
        self.key = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = self.head

        

    def get(self, key: int) -> int:

        if key in self.hashmap:
           node = self.hashmap[key]
           value = node.value
           self.del1(key)
           self.put(key, node.val)
           return value


        else:
            return -1    
           
        

    def put(self, key: int, value: int) -> None:

        
        if key in self.hashmap:
            self.del1(key)

        if len(self.hashmap) >= self.capacity:
            node = self.head.next
            self.del1(node.key)

        node = ListNode(value)
        node.key = key
        self.hashmap[key] = node        
        tail = self.tail
        tail.next =  node
        node.prev = tail
        self.tail = self.tail.next   



        
    def del1(self, key):
        node = self.hashmap[key]

        prev = node.prev
        nxt = node.next

        # connect previous to next
        prev.next = nxt

        if nxt:
            nxt.prev = prev
        else:
            # node was tail
            self.tail = prev

        del self.hashmap[key]



