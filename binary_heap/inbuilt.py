import heapq

class BinaryHeap:
    def __init__(self):
        self.heap=[]
    
    def insert(self,value):
        heapq.heappush(self.heap,value)
    
    def extract_min(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)
    
    def delete(self,value):
        try:
            self.heap.remove(value)
            heapq.heapify(self.heap)
        except ValueError as err:
            print(f'{value} not found in heap')
    
    def __str__(self):
        return '-'.join(map(str,self.heap))

bp=BinaryHeap()
bp.insert(10)
bp.insert(2)
bp.insert(5)
bp.insert(1)
bp.insert(8)
print(bp)
bp.delete(5)
print(bp)
