class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_list = {}
        for i in nums :
            hash_list[i] = 1 + hash_list.get(i ,0)
        heap = []
        for num, count in hash_list.items():
            heapq.heappush(heap,(count,num))
            if (len(heap) > k):
                heapq.heappop(heap)            

        ret = []
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])
        return ret            