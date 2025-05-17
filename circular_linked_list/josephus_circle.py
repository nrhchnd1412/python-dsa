class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def count(self):
        if not self.head:
            return 0
        else:
            count = 0
            current = self.head
            while True:
                count+=1
                current=current.next
                if current==self.head:
                    break
            return count

    def append(self,value):
        node=Node(value)
        if not self.head:
            self.head=node
            self.tail=node
            node.next=node
        else:
            self.tail.next=node
            node.next=self.head
            self.tail=node
        self.length+=1
    
    def __str__(self):
        result =''
        if self.head:
            current=self.head
            while True:
                result+=str(current.data)
                current=current.next
                if current==self.head:
                    break
                result+="->"
            return result

    def delete_node_by_key(self,key):
        if not self.head:
            return None
        if self.head.next ==self.head and self.head.data==key:
            self.head=None
            self.tail=None
            self.length=0
            return
        while self.head.data==key:
            self.head = self.head.next
            self.tail.next = self.head
            self.length-=1
        while True:
            prev=self.head
            current=self.head.next
            while current!=self.head:
                if current.data==key:
                    prev.next =current.next
                else:
                    prev=current
                current=current.next
            break

    def josephus_circle(self,step):
        temp=self.head
        while self.count()>1:
            count =1
            while count!=step:
                count+=1
                temp=temp.next
            print(f'removing node with data {temp.data}')
            self.delete_node_by_key(temp.data)
            print(f"count left {self.count()}")
            temp=temp.next
        print(f'Last standing player is {temp.data}')
            

c=CircularLinkedList()
c.append(1)
c.append(2)
c.append(3)
c.append(4)
c.append(5)
c.append(6)
print(c)

c.josephus_circle(3)
