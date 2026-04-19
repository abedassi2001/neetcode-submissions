class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 1 
        right = len(numbers)  
        #[1,2,3,4,5,6] target = 3
        while left < right :
            if numbers[left - 1] + numbers[right - 1] > target :
                right -= 1
            elif numbers[left - 1] + numbers[right - 1 ] < target :
                left += 1
            else :
                return [left , right]
        return [0,0]                                