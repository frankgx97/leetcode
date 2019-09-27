class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.data.keys():
            self.data[number] = 1
        else:
            self.data[number] += 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for i in self.data.keys():
            if value-i in self.data.keys():
                if value-i == i:
                    if self.data[i] > 1:
                        return True
                else:
                    return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
