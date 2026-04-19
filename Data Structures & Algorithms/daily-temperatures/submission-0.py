class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = deque()

        helper = [[index,value,0] for index , value in enumerate(temperatures)]
        for i in range(len(helper)) :
            print(stack)
            if len(stack) > 0:
                print((helper[i][1],i))
                print((stack[-1][1],i))
                while helper[i][1] > stack[-1][1]:
                    helper[stack[-1][0]][2] =  helper[i][0] - stack[-1][0]
                    stack.pop()
                    if len(stack) == 0 :
                        break

            stack.append(helper[i]) 

        ret = [helper[i][2] for i in range(len(helper))]   

        return ret             


            
        