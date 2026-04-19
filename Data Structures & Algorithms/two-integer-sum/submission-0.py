class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_box = {}
        for  index,value in enumerate(nums) : 
            if(hash_box.get(target-value) != None):
                return [hash_box[target-value],index]
            hash_box[value] = index
        return [0,0]                            