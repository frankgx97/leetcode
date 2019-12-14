class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        merge sort - ac
        time: O(nlogn)
        '''    
        def merge(l,r):
            ret = []
            while l and r:
                if l[0] <= r[0]:
                    ret.append(l.pop(0))
                else:
                    ret.append(r.pop(0))
            if l:
                ret += l
            elif r:
                ret += r
            return ret
        
        def ms(arr):
            if len(arr) <= 1:
                return arr
            l = 0
            r = len(arr)-1
            mid = l+(r-l)//2
            l = ms(arr[:mid+1])
            r = ms(arr[mid+1:])
            return merge(l,r)
        return ms(nums)
