class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
        two pointers - ac
        time O(n)
        space O(1)
        '''
        left = 0
        right = 0
        while right <= len(chars):
            if right == len(chars) or chars[left] != chars[right]:
                if right > left+1:
                    intstr = str(right - left)
                    left += 1
                    for i in intstr:
                        chars[left] = i
                        left += 1
                    while left < right:
                        chars.pop(left)
                        right -= 1
                left = right
                if right == len(chars):
                    break
            elif chars[left] == chars[right]:
                right +=1
        return len(chars)
