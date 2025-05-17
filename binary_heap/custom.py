class BinaryHeap:
    def __init__(self):
        self.heap=[]

    def get_heap_length(self):
        return len(self.heap)

    def __str__(self):
        return '-'.join(map(str,self.heap))

    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
    
    def delete(self,value):
        try:
            index=self.heap.index(value)
            if index<self.get_heap_length():
                self.heap[index]=self.heap.pop()
                self.heapify_down(index)
                self.heapify_up(index)
        except ValueError as err:
            print('Element not found in heap')

    def extract_min(self):
        if not self.heap:
            print('Empty heap')
            return None
        item = self.heap[0]
        last_el = self.heap.pop()
        if self.heap:
            self.heap[0]=last_el
            self.heapify_down(0)
        return item

    def get_minimum(self):
        if not self.heap:
            print('Heap empty')
            return None
        return self.heap[0]
    
    def heapify_up(self,index):
        while index>0:
            parent=(index-1)//2
            if self.heap[parent]>self.heap[index]:
               self.heap[parent], self.heap[index]=self.heap[index],self.heap[parent]
               index=parent 
            else:
                break

    def heapify_down(self,index):
        size = self.get_heap_length()
        while(left:=2*index+1) < size:
            smallest = left
            right = left+1
            if right<size and self.heap[right]<self.heap[left]:
                smallest=right
            if self.heap[index]>self.heap[smallest]:
                self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]
                index=smallest
            else:
                break

h=BinaryHeap()
h.insert(10)
h.insert(2)
h.insert(5)
h.insert(1)
h.insert(8)
print(h)
print('\n after deletion')
h.delete(5)
print(h)