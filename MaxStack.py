class MaxStack:
    '''
    two stack - ac
    time : popMax O(n), others O(1)
    caution: when implementing popMax(), use existing methods to ensure s2 is updated
    ref: https://paste.ubuntu.com/p/Zt6kzGCR9m/
    '''

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        '''
        directly push to s1
        if current item is larger than top of s2, push current item to s2,
        otherwise push the top of s2 again.
        '''
        self.s1.append(x)
        if not self.s2 or x > self.s2[-1]:
            self.s2.append(x)
        else:
            self.s2.append(self.s2[-1])
        return
        

    def pop(self) -> int:
        '''
        pop both s1 and s2
        '''
        x = self.s1.pop(-1)
        self.s2.pop(-1)
        return x
        

    def top(self) -> int:
        return self.s1[-1]
        

    def peekMax(self) -> int:
        return self.s2[-1]
        

    def popMax(self) -> int:
        '''
        use a temp stack
        pop until reach the max item, then push popped items back to the stack.
        '''
        ma = self.s2[-1]
        temp = []
        while self.top() != ma:
            temp.append(self.pop())
            
        x = self.pop()
        while temp:
            self.push(temp.pop(-1))
        return x
            
        
        
'''
    heap method does not work in popMax

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.heap = []
        
        

    def push(self, x: int) -> None:
        self.data.append(x)
        heapq.heappush(self.heap,-x)
        return
        

    def pop(self) -> int:
        x = self.data.pop(-1)
        if self.heap and self.heap[0] == -x:
            heapq.heappop(self.heap)
        return x
        

    def top(self) -> int:
        return self.data[-1]
        

    def peekMax(self) -> int:
        return -self.heap[0]
        

    def popMax(self) -> int:
        print(self.data)
        print(self.heap)
        for i in range(len(self.data)-1, -1, -1):
            #print(i)
            if self.data[i] == -self.heap[0]:
                x = self.data.pop(i)
                heapq.heappop(self.heap)
                return x
'''

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
