class Solution:
    def isHappy(self, n: int) -> bool:
        history = []
        curr = str(n)
        
        while curr != '1':
            current_sum = 0
            for i in curr:
                current_sum += int(i)**2
            curr = str(current_sum)
            if curr in history:
                return False
            else:
                history.append(curr)
        return True
