class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [i for i in nums]
        right = [j for j in nums]
        size = len(nums)

        for x in range(size):

            if x > 0 : 
                left[x] *= left[x - 1]
                
                right[size - x - 1] *= right[ size - x ]

                

        print(right)
        print(left)
        for l in range(size):

            if l == 0 :
                nums[l] = right[l + 1]
            elif l == size - 1:
                nums[l] = left[l - 1]
            else :
                nums[l] = left[l - 1] * right[l + 1]

        return nums                                

