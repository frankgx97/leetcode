import heapq
class MinStack:
    '''
    two stack - ac
    use two stacks ,s1 and s2
    s1 is a normal list to store the stack items
    the incoming item only be pushed in to stack when incoming item is smaller than top of s2
    '''

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        if not self.s2 or self.s2[-1] >= x:
            self.s2.append(x)
        return
        

    def pop(self) -> None:
        x = self.s1.pop(-1)
        if self.s2 and self.s2[-1] == x:
            self.s2.pop(-1)
        return
        

    def top(self) -> int:
        return self.s1[-1]
        

    def getMin(self) -> int:
        return self.s2[-1]
