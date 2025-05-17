'''
Queue in python using Linked lists
'''

class Node:
    def __init__(self,value,next=None):
        self.data=value
        self.next=next

class Queue:
    def __init__(self):
        self.head=None
        self.length=0
    
    def __str__(self):
        temp=self.head
        result=""
        while temp:
            result+=str(temp.data)
            temp=temp.next
            if not temp:
                break
            result+=" <- "
        return result

    def enque(self,value):
        node=Node(value)
        if not self.head:
            self.head=node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=node
            node.next=None
        self.length+=1

    def is_empty(self):
        return self.head is None
    
    def deque(self):
        if self.is_empty():
            print('queue is empty')
            return
        item = self.head
        self.head=self.head.next
        self.length-=1
        return item

q=Queue()
q.enque(1)
q.enque(2)
q.enque(3)

print(q)

q.deque()

print(q)