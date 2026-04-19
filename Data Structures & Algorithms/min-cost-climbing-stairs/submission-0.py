class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        costs = [ 0 for i in range (len(cost) )]

        for i in range (len(costs) ) :
            print(i)
            print(costs) 
            if i == 0 or i == 1 : 
                costs[i] = cost[i]
            else :
                costs[i] = min(costs[i - 1] + cost[i] , costs[i - 2] + cost[i])  
        print(costs)                
        return min(costs[-1] , costs[-2])                                


        