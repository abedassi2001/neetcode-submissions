class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_list = {}

        for i in nums :
            if hash_list.get(i) == 1:
                return True
            hash_list[i] = 1
        return False            
        