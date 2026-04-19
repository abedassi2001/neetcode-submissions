class Solution:
    def rob(self, nums: List[int]) -> int:
        # to rob good we need to rob the maximum betwen the last 2 before me 
        if len(nums) == 0 :
            return 0
        if len(nums) == 1 :
            return nums[0]            
        for index , num in enumerate(nums):
            if index == 0 or index == 1 : 
                continue 
            if index == 2 :
                nums[index] = max(nums[index - 2] + num , nums[index - 1] )
                continue                
            nums[index] = max(nums[index - 2] + num , nums[index - 1] , nums[index - 3 ] + num)
        print(nums)            
        return  max (nums[-1], nums[1] , nums[0])                             

        