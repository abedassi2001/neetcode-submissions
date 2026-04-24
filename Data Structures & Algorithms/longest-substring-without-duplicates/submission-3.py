class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0 
        s_arr = list(s)
        length = 0 
        max_length = 0
        s_map = {}

        for i in range(len(s_arr)):

            if s[i] in s_map :
                to_del_index = s_map[s[i]]

                for j in range(start , to_del_index):
                    del s_map[s[j]]

                start = to_del_index + 1 

            s_map[s[i]] = i
            length = i - start + 1                  
            max_length = max(length , max_length)


        return max_length             




            
