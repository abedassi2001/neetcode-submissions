class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max = 0 
        max_profit = 0
        curr_min = math.inf
        #[10,1,5,6,7,1]
        for i in prices :
            curr_max = max(curr_max , i)
            print(max_profit)                
            if i < curr_min :
                print(" i got here " )
                max_profit = max(curr_max - curr_min , max_profit)
                curr_max = 0 
                curr_min = i
        return max (max_profit, curr_max - curr_min)
                