# Time Optimized solution

class MedianFinder:

    def __init__(self):
        
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1*num)
        
        # make sure every num small is <= every num in large
        if (self.small and self.large and (-1*self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # uneven size ?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1*self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()




# Memory Optimized solution - Beats 99.36% 

class MedianFinder:

    def __init__(self):
        
        self.array = []

    def addNum(self, num: int) -> None:
        
        self.array.append(num)

    def findMedian(self) -> float:
        
        self.array.sort()
        l = len(self.array)

        if l % 2 == 0:
            return (self.array[(l-1) // 2] + self.array[((l-1) // 2) + 1]) / 2
        elif l % 2 != 0:
            return self.array[(l - 1) // 2]  