'''
Using a binary heap to perform sorting and finding the kth largest or smallest element in a list
'''

class BinaryHeap:
    def __init__(self):
        self.heap=[]
    
    def heapify_up(self,index):
        if not self.heap:
            return None
        while index>0:
            parent = (index-1)//2
            if self.heap[parent]>self.heap[index]:
                self.heap[parent],self.heap[index]=self.heap[index],self.heap[parent]
                index=parent
            else:
                break

    def heapify_down(self,index):
        if not self.heap:
            return None
        while(left:=2*index+1)< len(self.heap):
            smallest=left
            right = left+1
            if right<len(self.heap) and  self.heap[right]<self.heap[left]:
                smallest=right
            if self.heap[index]>self.heap[smallest]:
               self.heap[index], self.heap[smallest]= self.heap[smallest],self.heap[index]
               index=smallest
            else:
                break

    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
    
    def extract_min(self):
        if not self.heap:
            return None
        item= self.heap[0]
        last_el = self.heap.pop()
        if self.heap:
            self.heap[0]=last_el
            self.heapify_down(0)
        return item
    
    def get_minimum(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    def get_heap_size(self):
        return len(self.heap)

def sort(my_arr):
        heap=BinaryHeap()
        if not my_arr:
            return []
        for item in my_arr:
            heap.insert(item)
        sorted=[]
        while len(heap.heap)>0:
            sorted.append(heap.extract_min())
        return sorted
    
def find_n_smallest(my_arr,n):
        heap=BinaryHeap()
        if not my_arr or n<=0:
            return []
        for item in my_arr:
            heap.insert(item)
        result=[]
        for _ in range(min(n,heap.get_heap_size())):
            result.append(heap.extract_min())
        return result
    
def find_k_largest(my_arr,k):
        heap=BinaryHeap()
        if not my_arr or k<=0:
            return []
        for item in my_arr:
            if heap.get_heap_size()<k:
                heap.insert(item)
            else:
                smallest_yet= heap.get_minimum()
                if smallest_yet is not None and item>smallest_yet:
                    heap.extract_min()
                    heap.insert(item)
        result=[]
        while heap.get_heap_size()>0:
            result.append(heap.extract_min())
        
        return result[::-1]

    
my_arr=[6,4,5,1,3,2,7]
print(sort(my_arr))
print(find_n_smallest(my_arr,2))
print(find_k_largest(my_arr,2))