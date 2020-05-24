class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:'
        '''
        two pointer
        取左侧最大，取右侧最小，如果左侧小于等于右侧，就加答案
        然后舍弃右侧最小的，加指针
        '''
        i = j = 0
        ans = []
        while i < len(A) and j < len(B):
            l = max(A[i][0],B[j][0])
            r = min(A[i][1],B[j][1])
            if l <= r:
                ans.append([l,r])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return ans
                
