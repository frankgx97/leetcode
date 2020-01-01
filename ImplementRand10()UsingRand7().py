# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    '''
    Rejection Sampling - ac
    ref: https://blog.csdn.net/fuxuemingzhu/article/details/81809478
    
    '''
    def rand10(self):
        """
        :rtype: int
        """
        def rand49():
            return 7 * (rand7() - 1) + rand7() - 1
        def rand40():
            n = rand49()
            while n >= 40:
                n = rand49()
            return n
        return rand40() % 10 + 1
