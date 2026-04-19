class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range (len(nums))  :
            nums[i] -= 1 
        for  i in range (len(nums)) :
            print(nums) 
            if(nums[i] == nums[nums[i]] and i != nums[i] ):
                return nums[i] + 1  

            else :
                temp = nums[nums[i]]
                nums[nums[i ]] = nums[i]
                nums[i] = temp 

        return nums[i] + 1                                  
        