class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        counter = 0
        for string in strs :
            ret += string
            ret += "/"
        return ret         
    def decode(self, s: str) -> List[str]:
        counter = 0
        i = 0 
        j = 0  
        for let in s :
            if let == "/":
                counter += 1
        ret_list = [  ""for i in range(counter)]
        while  i < len(s):
            if(s[i ] == "/"):
                j += 1
            else :
                ret_list[j] += s[i]           
            i += 1
        return ret_list                            
