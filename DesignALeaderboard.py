class Leaderboard:

    def __init__(self):
        self.hashmap = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.hashmap:
            self.hashmap[playerId] = score
        else:
            self.hashmap[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for i in self.hashmap:
            heapq.heappush(heap, -self.hashmap[i])
        i = 0
        summ = 0
        while i < K:
            score = heapq.heappop(heap)
            score = 0 - score
            summ += score
            i += 1
        return summ
                
    def reset(self, playerId: int) -> None:
        self.hashmap[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
