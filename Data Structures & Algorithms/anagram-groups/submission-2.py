class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ret_list = defaultdict(list)

        for value in strs:
            curr_hash = {}
            for j in value:
                curr_hash[j] = 1 + curr_hash.get(j, 0)
            key = tuple(sorted(curr_hash.items()))
            ret_list[key].append(value)
        
        return list(ret_list.values())    
