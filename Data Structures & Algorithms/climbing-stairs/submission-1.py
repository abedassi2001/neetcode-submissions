class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 :
            return 1 
        if n == 0 : 
            return 0 
        if n == 2 :
            return 2                         
        ret_list = [ 0 for i in range(n)]
        ret_list[0] = 1
        ret_list[1] = 2
        for i in range(n) :
            if i - 1  > 0 and i - 2 >= 0 :
                ret_list[i] = ret_list[i - 1] + ret_list[i - 2]  
        print(ret_list)                
        return ret_list[n - 1]                 

