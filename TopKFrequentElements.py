class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            if i not in map.keys():
                map[i] = 1
            else:
                map[i] += 1

        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        for i in map.keys():
            bucket[map[i]].append(i)
        result = []
        c = 0
        i = len(nums)
        while i >= 0 and c < k:
            if bucket[i] == []:
                i-=1
                continue
            else:
                for j in bucket[i]:
                    c += 1
                    result.append(j)
                i-=1
        return result
