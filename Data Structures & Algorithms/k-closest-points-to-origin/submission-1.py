class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        i = 0 
        while i < k :
            heapq.heappush(heap,(-1 * ((points[i][0] ** 2) + (points[i][1] ** 2)),i))
            i += 1
        print(heap)
        while i < len(points) : 
            heapq.heappush(heap,( -1 *((points[i][0] ** 2) + (points[i][1] ** 2)),i))
            heapq.heappop(heap)
            i += 1 
        ret_list = []
        for i in heap :
            ret_list.append(points[i[1]])

        return ret_list
