class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        '''
        dfs - ac
        use visited set to prevent duplcation
        similar to number of islands
        '''
        m = len(image)
        n = len(image[0])
        starting = image[sr][sc]
        visited = set()
        def dfs(row,col):
            image[row][col] = newColor
            visited.add((row,col))
            if row+1 < m and image[row+1][col] == starting and (row+1,col) not in visited:
                dfs(row+1,col)
            if row-1 >= 0 and image[row-1][col] == starting and (row-1,col) not in visited:
                dfs(row-1,col)
            if col+1 < n and image[row][col+1] == starting and (row,col+1) not in visited:
                dfs(row,col+1)
            if col-1 >= 0 and image[row][col-1] == starting and (row,col-1) not in visited:
                dfs(row,col-1)
            return
        dfs(sr,sc)
        return image
