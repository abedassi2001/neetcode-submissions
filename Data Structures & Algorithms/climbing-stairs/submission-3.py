class Solution:
    def climbStairs(self, n: int) -> int:
     
        count = 0 

        if n == 0 : 
            return 0    
        if n == 1 :
            return 1
        if n == 2 :
            return 2 

        help_list = [0 for i in range(n)]

        help_list[0] = 1 
        help_list[1] = 2

        for i in range(2,len(help_list)):

            help_list[i] = help_list[i - 1 ] + help_list[ i - 2 ]

        return help_list[-1]




