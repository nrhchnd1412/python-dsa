class Node:
    def __init__(self,value,min,next=None):
        self.data=value
        self.next=next
        self.min=min

class LinkedList:
    def __init__(self):
        self.head=None
        self.length=0
    
    def __str__(self):
        result =""
        temp=self.head
        while temp:
            result+=str(temp.data)
            temp=temp.next
            if not temp:
                break
            result+=" -> "
        return result
    
    def push(self,value):
        if not self.head:
            node=Node(value,value)
        else:
            new_min = min(self.head.min,value)
            node=Node(value,new_min,self.head)
        self.head=node
        self.length+=1

    
    def pop(self):
        if not self.head:
            print('stack is empty')
            return
        item = self.head.data
        self.head=self.head.next
        self.length-=1
        return item

    def min_(self):
        if not self.head:
            print('Empty stack')
            return
        return self.head.min

l = LinkedList()
l.push(10)
l.push(5)
l.push(1)
l.push(0)
l.push(-1)
l.push(1)
l.push(100)
print(l)
print(l.min_())
l.pop()
l.pop()
l.pop()
print(l)
print(l.min_())

    

