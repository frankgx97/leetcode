class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, vi in enumerate(nums):
            if (target - vi) in hashmap.keys():
                if hashmap[target - vi] != i:
                    return [hashmap[target - vi],i]
            else:
                hashmap[vi] = i
            
