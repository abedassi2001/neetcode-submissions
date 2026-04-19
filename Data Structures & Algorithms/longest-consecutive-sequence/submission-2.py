class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        hash_map = {}
        for index , value in enumerate(nums) :
            hash_map[value] = index
        help_hash = {}
        i = 1
        for num , index in hash_map.items():
            counter = 1
            if num in help_hash :
                continue
            else :
                help_hash[num] = 1
                while hash_map.get(num + i) is not None :
                    print(num + i)
                    if help_hash.get(num + i) is not None  :
                        help_hash[num] += help_hash[num + i]
                        i = 1
                        break
                    else :
                        help_hash[num + i] = 1 
                        help_hash[num] += 1
                        i += 1
                i = 1
        print(help_hash)
        return max(help_hash.values())
                                                                         

