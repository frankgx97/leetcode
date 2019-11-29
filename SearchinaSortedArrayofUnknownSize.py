class Solution:
    def search(self, reader, target):
        '''
        binary search - ac
        
        O(log(n))
        '''
        """
        :type reader.get: Arrayreader.get
        :type target: int
        :rtype: int
        """
        def bs(left,right,target):
            while left <= right:
                mid = (left + right) //2
                if reader.get(mid) == target:
                    return mid
                elif reader.get(mid) > target:
                    right = mid -1 
                elif reader.get(mid) < target:
                    left = mid+1
            return -1
        
        left = 0
        right = 0
        flag = False
        i=0
        while reader.get(i) != 2147483647:
            if reader.get(i) == target:
                return i
            if reader.get(i) < target:
                left = i
            elif reader.get(i) > target:
                right = i
                flag = True
                break
            if i == 0:
                i+=1
            else:
                i*=50

        right = i
        return bs(left,right,target)
