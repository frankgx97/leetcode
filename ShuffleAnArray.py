import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.visited = set()
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.visited = set()
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        def rand():
            res = []
            candidates = [i for i in range(len(self.nums))]
            while candidates:
                rnd = random.randint(0,len(candidates)-1)
                res.append(self.nums[candidates.pop(rnd)])
            return res
                
        ans = rand()
        while tuple(ans) in self.visited:
            ans = rand()
        self.visited.add(tuple(ans))
        return ans
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
