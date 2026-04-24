class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        max_counter = 0
        start = 0
        max_length = 0
        
        # Use 'end' as the right pointer
        for end in range(len(s)):
            # 1. Expand: Add current character to map
            hash_map[s[end]] = 1 + hash_map.get(s[end], 0)
            
            # 2. Track the count of the most frequent character in the current window
            max_counter = max(max_counter, hash_map[s[end]])
            
            # 3. Shrink: If (window_size - max_freq_count) > k, it's invalid
            # Window size is (end - start + 1)
            while (end - start + 1) - max_counter > k:
                hash_map[s[start]] -= 1
                start += 1
            
            # 4. Result: The largest valid window we've seen
            max_length = max(max_length, end - start + 1)
            
        return max_length