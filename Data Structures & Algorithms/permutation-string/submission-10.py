from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_s1 = Counter(s1)

        start = 0 
        end = len(s1) 
        print(end)
        init_string = s2[0:end]
        the_hash = Counter(init_string)

        for i in range(end  ,len(s2)):
            print(the_hash)
           
            if the_hash == hash_s1 :
                return True
            
           
            the_hash[s2[start]] -= 1 

            if the_hash[s2[start]] == 0 :
                del the_hash[s2[start]]

            start += 1 

            if the_hash.get(s2[i]):
                the_hash[s2[i]] += 1

            else :
                the_hash[s2[i]] = 1                
            
        if the_hash == hash_s1 :
                return True
            
        return False                

                                                 




        