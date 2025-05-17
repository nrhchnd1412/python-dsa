'''
Stacks in python using Linked Lists
'''

class Node:
    def __init__(self,value,next=None):
        self.data=value
        self.next=next

class Stack:
    def __init__(self):
        self.head=None
        self.length=0
    
    def push(self,value):
        node=Node(value)
        if not self.head:
            self.head=node
        else:
            node.next = self.head
            self.head=node
        self.length+=1
    
    def pop(self):
        if not self.head:
            print('Stack is empty')
            return
        self.head=self.head.next
        self.length-=1
    
    def __str__(self):
        result =''
        temp=self.head
        while temp:
            result+=str(temp.data)
            temp=temp.next
            if not temp:
                break
            result+=" -> "
        return result

s= Stack()
s.push(1)
s.push(2)
s.push(3)

print(s)

s.pop()
print(s)