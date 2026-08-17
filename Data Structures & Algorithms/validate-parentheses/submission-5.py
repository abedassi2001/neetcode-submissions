from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        open_brackets = deque()     
        brackets = {
        ")" : "(" , 
        "]" :"[" ,
        "}" : "{"
        }

        for l in s : 

            if l in brackets : # if its closed bracket 
                if len(open_brackets) == 0 :
                    return False 
                    
                top = open_brackets.pop()
                
                if brackets[l] != top : 
                    return False 
            
            else :                    
                open_brackets.append(l)

        return True  if len(open_brackets) == 0 else False                                 






        