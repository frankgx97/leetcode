class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        '''
        memo = {}
        def dfs(curr, height,currheight, width_left):
            if (curr, height,currheight, width_left) in memo:
                return memo[(curr, height,currheight, width_left)]
            if curr == len(books):
                memo[(curr, height,currheight, width_left)] = height + currheight
                return height + currheight
            if books[curr][0] <= width_left:
                new = dfs(curr+1, height+currheight,books[curr][1], shelf_width-books[curr][0]) # start new row
                if books[curr][1] > currheight:
                    currheight = books[curr][1]
                cont = dfs(curr+1, height, currheight, width_left-books[curr][0]) # continue on current row
                memo[(curr, height,currheight, width_left)] = min(cont, new)
                return min(cont, new)
            else:
                r = dfs(curr+1, height+currheight,books[curr][1], shelf_width-books[curr][0])
                memo[(curr, height,currheight, width_left)] = r
                return r
        return dfs(0, 0, 0, shelf_width)
                
        '''
        memo = []
        for _ in range(len(books)+1):
            memo.append([0]*(shelf_width+1))
            
        def dfs(curr, height,width_left):
            if curr == len(books):
                return height
            if memo[curr][width_left] > 0:
                return memo[curr][width_left]
            
            r = float('inf')
            
            if books[curr][0] <= width_left:
                r = min(r, dfs(curr+1, max(books[curr][1], height),width_left - books[curr][0]))
            
            r = min(r, height+ dfs(curr+1, books[curr][1], shelf_width - books[curr][0]))
            memo[curr][width_left] = r
            return r
        return dfs(0, 0, shelf_width)
