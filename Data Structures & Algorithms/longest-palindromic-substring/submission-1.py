class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        start  , end = 0 , 0 
        max_length = 0
        def expand_center (left , right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1 
                right += 1 

            return right - left - 1 

        for i in range(len(s)):

            len1 = expand_center(  i , i)

            len2 = expand_center( i , i + 1)

            max_length = max(len1 , len2)

            if max_length > end - start  :

                start = i  - (max_length - 1 ) // 2
                end = i + max_length // 2  

        return s[start : end + 1 ]




                


                






        
        