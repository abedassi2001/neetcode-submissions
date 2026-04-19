
[0,1,4,7]
[1,2,2,1]
target = 10 

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        help_arr = []
        if len(position) == 0 :
            return 0
        for i in range(len(position)) :
            arrival_time = (target - position[i]) / speed[i]
            help_arr.append((position[i],   arrival_time))

        help_arr.sort(reverse = True)

        stack = deque()
        counter = 0
        print(help_arr)
        for index , value in enumerate(help_arr):
            if  not stack or value[1] > stack[-1] :
                stack.append(value[1])

        print(stack)
        return len(stack)                                   

