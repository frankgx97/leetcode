import heapq
class MinStack:
    '''
    heap - ac
    use heap to store the min
    when poping, check if the heap root is the same with popped item, if yes, pop the heap.
    '''

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap = []
        self.data = []
        

    def push(self, x: int) -> None:
        self.data.append(x)
        heapq.heappush(self.heap,x)
        return
        

    def pop(self) -> None:
        if self.data:
            x = self.data.pop(-1)
            if self.heap[0] == x:
                heapq.heappop(self.heap)
        return
        
        

    def top(self) -> int:
        if self.data:
            return self.data[-1]
        else:
            return -1
        

    def getMin(self) -> int:
        if self.heap:
            return self.heap[0]
        else:
            return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
