class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)

    def addNum(self, num: int) -> None:

        if len(self.max_heap) == 0 :
            heapq.heappush(self.max_heap ,  -1 *num)
            return 

        if num <= -1 *self.max_heap[0] :
            heapq.heappush(self.max_heap , -1 * num)

        else :
            heapq.heappush(self.min_heap , num)

        if len(self.max_heap ) - len(self.min_heap) >= 2 :
            swap = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap , -1 * swap)

        if len(self.min_heap )  -  len(self.max_heap) >= 1 : 
            swap = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap , -1 * swap)                                  

        

    def findMedian(self) -> float:

        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] +  -1 *self.max_heap[0]) / 2
        print(self.min_heap)
        print(self.max_heap)
        return -1 * self.max_heap[0]             

        
        