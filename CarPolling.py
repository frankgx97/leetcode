class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        min_location = 99999
        max_location = 0
        get_off = {}
        get_in = {}
        for i in trips:
            min_location = min(min_location, i[1], i[2])
            max_location = max(max_location, i[1], i[2])
            if i[1]in get_in.keys():
                get_in[i[1]] += i[0]
            else:
                get_in[i[1]] = i[0]
            if i[2] in get_off.keys():
                get_off[i[2]] += i[0]
            else:
                get_off[i[2]] = i[0]
            
        for location in range(min_location, max_location+1):
            if location in get_off.keys():
                capacity += get_off[location]
            if location in get_in.keys():
                if capacity >= get_in[location]:
                    capacity -= get_in[location]
                else:
                    return False
        return True
