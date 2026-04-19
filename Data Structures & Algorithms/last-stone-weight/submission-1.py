class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [ -x for x in stones]

        heapq.heapify(arr)
        if len(arr) == 0 : 
            return 0
        if len(arr) == 1 :
            return -1 * arr[0]            
        while len(arr) > 1:
            temp1 = heapq.heappop(arr)
            temp2 = heapq.heappop(arr)
            print(temp1)
            print(temp2)
            temp3 = temp1 - temp2
            print(temp3) 
            if temp3 < 0 :
                heapq.heappush(arr,temp3)
            print(arr)                
        if len(arr) == 0 :
            return 0
        else:
            return (-1 * arr[0])                            



        