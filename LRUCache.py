class Node:
    def __init__(self):
        self.k = None
        self.v = None
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.h = {}
        self.cap = 0
        self.maxcap = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.h.keys() or self.h[key] == None:
            return -1
        else:
            self.mth(key)
            #self.pr()
            return self.h[key].v

    def put(self, key: int, value: int) -> None:
        if key in self.h.keys() and self.h[key] != None:
            self.h[key].v = value
            self.mth(key)
            #self.pr()
            return
        if self.cap >= self.maxcap:
            self.rm_tail()
        self.insert_head(key,value)
        #self.pr()
        return
            
    def rm_tail(self):
        self.cap -= 1
        to_del = self.tail.prev
        temp = self.tail.prev.prev
        self.tail.prev = temp
        temp.next = self.tail
        self.h[to_del.k] = None
        #del(to_del)
        return
        
    def insert_tail(self,k,v):
        to_insert = Node()
        self.h[k] = to_insert
        to_insert.k = k
        to_insert.v = v
        
        last = self.tail.prev
        last.next = to_insert
        to_insert.prev = last
        to_insert.next = self.tail
        self.tail.prev = to_insert
        self.cap += 1
        return
    
    def insert_head(self,k,v):
        to_insert = Node()
        self.h[k] = to_insert
        to_insert.k = k
        to_insert.v = v
        
        first = self.head.next
        first.prev = to_insert
        to_insert.prev = self.head
        to_insert.next = first
        self.head.next = to_insert
        self.cap += 1
        return
    
    def mth(self,k):
        this = self.h[k]
        pre = this.prev
        nex = this.next
        pre.next = nex
        nex.prev = pre
        
        first = self.head.next
        
        self.head.next = this
        this.next = first
        this.prev = self.head
        first.prev = this
        
        return
    
    def pr(self):
        print('====')
        current = self.head.next
        while current.next != None:
            print(current.k,',',current.v,'|',end='')
            current = current.next
        print('------')
        return
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
