class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        dfs with pruning - ac
        perform dfs on the board - will tle without pruning
        - use a depth parameter to trace the depth of the search
            - if depth exceed the word length, return
            - if the word[depth] not equal to current seaching item, return
        - I use list to store the visited tuples, using set instead can be faster
        - but we need manually copy set to each recursion parameter, I did not see significant improvement
        - iterate the board, if current item == the start of the word, start a dfs here.
        
        time complexity: O(m*n*4^k) (k is the length of word)- in each dfs, we traval every node on the worst case
        ref: https://cs.stackexchange.com/questions/96626/whats-the-big-o-runtime-of-a-dfs-word-search-through-a-matrix
        space complexity: O(k) - the depth of the search
        '''
        m = len(board)
        n = len(board[0])
        def dfs(x,y,path,visited,depth):
            if path == list(word):
                return True
            if not 0<=x<m or not 0<=y<n:
                return False
            if (x,y) in visited:
                return False
            if depth > len(word):
                return False
            if word[depth] != board[x][y]:
                return False
            
            return dfs(x+1,y,path+[board[x][y]],visited+[(x,y)],depth+1) or \
            dfs(x,y+1,path+[board[x][y]],visited+[(x,y)],depth+1) or \
            dfs(x-1,y,path+[board[x][y]],visited+[(x,y)],depth+1) or \
            dfs(x,y-1,path+[board[x][y]],visited+[(x,y)],depth+1)
            
        for i in range(m):
            for j in range(n):
                if(board[i][j] == word[0]):
                    if dfs(i,j,[],[],0):
                        return True
                    else:
                        continue
        return False
