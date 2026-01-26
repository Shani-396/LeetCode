class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        mid = - self.max_heap[0] if self.max_heap else num
        if num <= mid:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap,  num)
        
        # Balance
        if len(self.max_heap) == len(self.min_heap) + 2:
            num = - heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, num)
        elif len(self.max_heap) + 1 == len(self.min_heap):
            num =   heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, - num)

    def findMedian(self) -> float:
        mid_1 = - self.max_heap[0]
        if len(self.max_heap) + len(self.min_heap) & 1:
            return mid_1
        return (mid_1 + self.min_heap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()