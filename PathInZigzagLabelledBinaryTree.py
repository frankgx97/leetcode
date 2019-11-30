class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        '''
        math - ac
        first try locating the target number(layer and index)
        then locate its parent(layer-1, index//2)
        until reach root
        '''
        target = label
        layer = 1
        largest_in_curr_layer = 1
        while largest_in_curr_layer < target:
            largest_in_curr_layer = 2**layer - 1
            layer += 1
        
        layer -= 1
        
        index_of_target = 0
        if layer % 2 == 0:
            #even  reversed
            index_of_target = 2**(layer) - 1 - target
        else:
            index_of_target = target - 2**(layer-1)

        curr = target
        r = []
        while curr > 1:
            r.append(curr)
            layer -= 1
            index_of_target //= 2
            if layer % 2 == 0:
                #even layer, reversed
                curr = 2**(layer) - 1 - index_of_target
            else:
                curr = 2**(layer-1) + index_of_target
        r += [1]
        return r[::-1]
