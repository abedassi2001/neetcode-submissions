class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_list1 = {}
        hash_list2 = {}
        for i in s :
            if hash_list1.get(i) is None :
                hash_list1[i] = 1 
            else : 
                hash_list1[i] += 1
        for i in t :
            if hash_list2.get(i) is None :
                hash_list2[i] = 1 
            else : 
                hash_list2[i] += 1

        return (hash_list1 == hash_list2)
