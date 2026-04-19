class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ret_num = [  0 for i in range(len(points))]
        for i in range(len(points)):
            ret_num[i] = (points[i][0] ** 2) + (points[i][1] ** 2) 
        print(ret_num)  

        heap = []
        heapq.heapify(heap)
        ret_val = []
        for  i in range(len(ret_num)):
            heapq.heappush(heap,(ret_num[i],i))
        for i in range(k):
             ret = heapq.heappop(heap)
             ret_val.append(points[ret[1]]) 
        return ret_val                                   