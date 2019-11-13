import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        heap - ac
        use a max heap, when iterating through the list, add the new item to the heap,
        and pop the top item in the heap if this item is not in the window anymore
        '''
        if not nums:
            return []
        
        heap = []
        for i in range(k):
            heapq.heappush(heap, -nums[i])
            
        i=1
        j=i+k-1
        m = [-heap[0]]
        while j<len(nums):
            while len(heap) > 0 and -heap[0] not in nums[i:j+1]:
                heapq.heappop(heap)
            heapq.heappush(heap,-nums[j])
            m.append(-heap[0])
            i+=1
            j+=1
        return m
