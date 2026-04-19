class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()

        for bracket in s :
            if bracket == "}" or bracket == "]" or bracket == ")":
                check = self.isMatch(stack, bracket)
                if check == True :
                    stack.pop()
                else :
                    return False
            else :
                stack.append(bracket) 
        if len(stack) != 0 :
            return False                
        return True

    def isMatch(self , stack , closed_bracket):
        if len(stack) == 0 :
            return False
        if closed_bracket == "}":
            if stack[-1] == "{":
                return True
            else :
                return False                
        if closed_bracket == "]":
            if stack[-1] == "[":
                return True
            else :
                return False 
        if closed_bracket == ")":
            if stack[-1] == "(":
                return True
            else :
                return False
        return True                                                         
        