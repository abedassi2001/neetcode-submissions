class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_hash = {}
        for num in nums :
            freq_hash[num] = 1 + freq_hash.get(num ,0)

        val_hash =[[]  for i in range (len(nums))]

        for num , count in freq_hash.items():
            if num not in val_hash[count -1 ]:
                val_hash[count -1 ].append(num)
        counter = k
        ret_list = []
        for iter in range(len(val_hash)):
            if counter == 0 :
                break
            if val_hash[len(val_hash) - iter -1] is not None :
                for string in val_hash[len(val_hash) - iter -1 ] :
                    if(counter == 0):
                        break
                    ret_list.append(string )
                    counter -= 1 
        return ret_list                                                               
