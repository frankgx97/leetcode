# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        '''
        dfs with stack
        corner case: [[[]],3]
        handle the nested cases in the "hasNext" method.
        do not invoke "next" method if there's not valid integer in current list
        otherwise we will get a "none" return value
        '''
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.d = nestedList
        self.stack = []
        for i in range(len(self.d)-1,-1,-1):
            self.stack.append(self.d[i])


    def next(self):
        """
        :rtype: int
        """
        while self.stack:
            curr = self.stack.pop(-1)
            if curr.isInteger():
                return curr.getInteger()
        return None
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            if not self.stack[-1].isInteger() and not self.stack[-1].getList():
                self.stack.pop(-1)
                continue
            elif self.stack[-1].isInteger():
                return True
            else:
                glist = self.stack.pop(-1).getList()
                for i in range(len(glist)-1,-1,-1):
                    self.stack.append(glist[i])
                continue
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
