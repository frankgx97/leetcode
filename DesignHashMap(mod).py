class MyHashMap:
    '''
    use mod as hashing function
    '''
    
    def __hashing(self, input):
        return input % 100000

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = []
        for i in range(100000):
            self.d.append([])
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        h = self.__hashing(key)
        for i in range(len(self.d[h])):
            if self.d[h][i][0] == key:
                print('update')
                self.d[h][i][1] = value
                return
        self.d[h].append([key,value])
        return
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        h = self.__hashing(key)
        for i in range(len(self.d[h])):
            if self.d[h][i][0] == key:
                return self.d[h][i][1]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        h = self.__hashing(key)
        i = 0
        while i < len(self.d[h]):
            if self.d[h][i][0] == key:
                self.d[h].pop(i)
                i+=1
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
