class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        max_length = 0
        s_map = {}

        for i in range(len(s)):
            char = s[i]

            # Logic: If we find a duplicate, clean the map from 'start' up to the duplicate
            if char in s_map:
                to_del_index = s_map[char]
                
                # IMPORTANT: Delete everything from the current start up to the duplicate
                # This physically shrinks your "window" in the dictionary
                for j in range(start, to_del_index):
                    del s_map[s[j]]
                
                # Move start to one position after the old duplicate
                start = to_del_index + 1
            
            # Update/Insert the current character
            s_map[char] = i
            
            # Logic: The window size is simply (current_index - start + 1)
            current_len = i - start + 1
            if current_len > max_length:
                max_length = current_len

        return max_length