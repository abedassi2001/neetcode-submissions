class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        for i in range (len(cost) ) :
            print(i)
            if i == 0 or i == 1 : 
                cost[i] = cost[i]
            else :
                cost[i] = min(cost[i - 1] + cost[i] , cost[i - 2] + cost[i])  
             
        return min(cost[-1] , cost[-2])                                


        