from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        #two heaps-large,small,minheap,maxheap
        self.a=SortedList()
        self.n=0

    def addNum(self, num: int) -> None:
        self.a.add(num)
        self.n+=1


    def findMedian(self) -> float:
        if self.n%2==0:
            return (self.a[self.n//2-1]+self.a[self.n//2])/2
        else:
            return self.a[self.n//2]
        
        