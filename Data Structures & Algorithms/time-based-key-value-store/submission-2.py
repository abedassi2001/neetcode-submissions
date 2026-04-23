class TimeMap:

    def __init__(self):
        self.hash = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.hash.get(key) :
            self.hash[key] = [(timestamp , value)]

        else :
            self.hash[key].append((timestamp, value))            


    def get(self, key: str, timestamp: int) -> str:
        if not self.hash.get(key) :
            return ""

        index = self.find_time(self.hash.get(key) , timestamp)
        if timestamp < self.hash[key][index][0]:
            return ""
        return self.hash[key][index][1]
        
    def find_time(self ,time_stamps , time_stamp):
        right = len(time_stamps) - 1 
        left = 0

        while left <= right : 
            mid = (right + left) // 2

            if time_stamps[mid][0] == time_stamp :
                return mid

            elif  time_stamps[mid][0] < time_stamp :
                left = mid + 1

            else :
                right = mid - 1

        return right                                                       
