class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        '''
        bfs + heap
        time: nlogn
        space: n
        '''
        def bfs(start):
            queue = [start]
            current_level = 0
            visited = set()
            while queue:
                if current_level >= level:
                    break
                subqueue = queue[:]
                queue = []
                for i in subqueue:
                    visited.add(i)
                    for j in friends[i]:
                        if j not in visited and j not in queue and j not in subqueue:
                            queue.append(j)
                current_level += 1
            return queue
        from collections import Counter
        import heapq
        videos = []
        for i in bfs(id):
            videos += watchedVideos[i]
        freq = dict(Counter(videos))
        heap = []
        for key in freq:
            heapq.heappush(heap, (freq[key], key))
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans
