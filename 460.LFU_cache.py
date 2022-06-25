class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None
        
class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.freq = {}
        
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right.next
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            if key in freq:
                self.freq[key] += 1
            else:
                self.freq[key] = 1
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if key in freq:
            self.freq[key] += 1
        else:
            self.freq[key] = 1
            
        if len(self.cache) > self.cap:
            least = min(self.cache.values())
            least_key = [key for key in self.cache if self.cache[key] == least]
            
            if len(least_key) == 1:
                self.remove(self.cache[least_key[0]])
                del self.cache[least_key[0]]
            else:
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)