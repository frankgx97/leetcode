class Solution:
    def primePalindrome(self, N: int) -> int:
        '''
        ac
        use two healper to see if current num is palindrome and prime
        skip the 10^7 - 10^8 range, because there's no prime in this range
        '''
        def is_palindrome(n):
            n = str(n)
            l = 0
            r = len(n) - 1
            while l<=r:
                if n[l] != n[r]:
                    return False
                else:
                    l+=1
                    r-=1
            return True
            
        
        def is_prime(n):
            if n == 1 or n == 0:
                return False
            for i in range(2,int(n**(0.5))+1):
                if n%i == 0:
                    return False
            return True
        
        i = N
        while not is_palindrome(i) or not is_prime(i):
            if 10**7 < i < 10**8:
                i = 10**8
            i+=1
        return i
