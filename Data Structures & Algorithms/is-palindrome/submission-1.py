class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        cleaned = ''.join([ch for ch in s.lower() if ('a' <= ch <= 'z') or ('0' <= ch <= '9')])
        print(s)
        right = len(cleaned) - 1                
        while left <= right :
            print(s[left])
            print(s[right]) 
            if cleaned[left].lower() != cleaned[right].lower():
                return False
            left += 1
            right -= 1
        return True            