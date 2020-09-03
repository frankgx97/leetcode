class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        def combines(s1,s2):
            total = len(s1) + len(s2)
            choose = len(s1)
            return math.comb(total,choose)
        
        def dfs(array):
            if not array:
                return 1
            root = array[0]
            left = []
            right = []
            for i in array:
                if i < root:
                    left.append(i)
                elif i > root:
                    right.append(i)
            ans_left = dfs(left)
            ans_right = dfs(right)
            return ans_left * ans_right * combines(left,right)
        return (dfs(nums) - 1 ) % mod
