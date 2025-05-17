'''
Queue in python using Lists
'''

class Queue:
    def __init__(self):
        self.queue=[]
    def __str__(self):
        return '<-'.join(map(str,self.queue))
    def enque(self,value):
        self.queue.append(value)
    def is_empty(self):
        return not bool(self.queue)
    def deque(self):
        if self.is_empty():
            print('Queue is empty')
            return
        self.queue.pop(0)

q=Queue()
q.enque(1)
q.enque(2)
q.enque(3)

print(q)

q.deque()

print(q)
