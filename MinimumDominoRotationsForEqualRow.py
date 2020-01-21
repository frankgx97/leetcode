class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        '''
        ac
        the number in each position either == a or == b
        '''
        for possibility in [A[0],B[0]]:
            at, bt = 0,0
            for a, b in zip(A,B):
                if possibility not in (a,b):
                    break
                if b != possibility:
                    at += 1
                if a != possibility:
                    bt += 1
            else:
                return min(at,bt)
        return -1
