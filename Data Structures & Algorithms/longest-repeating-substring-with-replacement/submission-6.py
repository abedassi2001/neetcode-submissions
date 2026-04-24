class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        max_counter = 0
        start = 0
        max_length = 0
        
        for end in range(len(s)):
            hash_map[s[end]] = 1 + hash_map.get(s[end], 0)
            
            max_counter = max(max_counter, hash_map[s[end]])
            

            if (end - start + 1) - max_counter > k:
                hash_map[s[start]] -= 1
                start += 1
            
            max_length = max(max_length, end - start + 1)
            
        return max_length