class CircularQueue:
    def __init__(self,max_size=6):
        self.queue=[None]*max_size
        self.max_size=max_size
        self.front=-1
        self.rear=-1
    
    def is_full(self):
        return (self.rear+1)%self.max_size == self.front

    def is_empty(self):
        return self.front==-1

    def __str__(self):
        result = []
        if self.is_empty():
            print('Circular Queue is empty')
        if self.front<=self.rear:
            result = self.queue[self.front:self.rear+1]
        else:
            result = self.queue[self.front:]+ self.queue[:self.rear+1]
        return '<-'.join(map(str,result))
    
    def enque(self,value):
        if self.is_full():
            print('Circular Queue is full')
            return
        if self.front==-1:
            self.front=0
        self.rear = (self.rear+1) % self.max_size
        self.queue[self.rear]=value

    def deque(self):
        if self.is_empty():
            print('Circular Queue is empty')
        item = self.queue[self.front]
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front = (self.front+1)% self.max_size
        return item


c=CircularQueue()
c.enque(1)
c.enque(2)
c.enque(3)
c.enque(4)
c.enque(5)
c.enque(6)

c.deque()
c.deque()

c.enque(81)

print(c)
