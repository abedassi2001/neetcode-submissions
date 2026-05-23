class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_sum = 0
        big_sum = -float('inf') 


        for i in range(len(nums)):
            curr_sum += nums[i]             
            
            big_sum = max(curr_sum , big_sum)

            if curr_sum <= 0 : 
                curr_sum = 0

        return big_sum            





            
        