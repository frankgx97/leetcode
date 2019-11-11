class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        ac
        use local_min and local_max to maintain the local min and max
        iterate the array
        if current < local_max, sell current stock if local_max > local_min
        then reset min and max
        if current is larger than local max, update max
        after the iteration, if local_max > local_min, sell the current stock.
        '''
        if not prices:
            return 0
        local_min = prices[0]
        local_max = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            print(prices[i], local_max, local_min)
            if prices[i] < local_max:
                #sell previous and reset min and max
                if local_max > local_min:
                    profit = profit + (local_max - local_min)
                local_min = prices[i]
                local_max = prices[i]
            if prices[i] > local_max:
                #reset max
                local_max = prices[i]
        if local_max > local_min:
            profit = profit + (local_max - local_min)
        return profit
