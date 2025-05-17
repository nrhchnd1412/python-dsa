class Node:
    def __init__(self,value,next=None):
        self.data=value
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
        self.length=0

    def append(self,value):
        node=Node(value)
        if not self.head:
            self.head=node
        else:
            temp = self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=node
            node.next=None
        self.length+=1
    
    def __str__(self):
        temp=self.head
        result=''
        while temp:
            result+=str(temp.data)
            temp=temp.next
            if not temp is None:
                result+="->"
        return result

    def remove_duplicates(self):
        if not self.head:
            return None
        track =set()
        track.add(self.head.data)
        prev=self.head
        current = self.head.next
        while current:
            if current.data in track:
                prev.next=current.next
                self.length-=1
            else:
                track.add(current.data)
                prev=current
            current=current.next

    def kth_element_from_last(self,k):
        if not self.head:
            return None
        p1=self.head
        p2=self.head
        for _ in range(k):
            if p2 is None:
                return None
            p2=p2.next
        while p2:
            p2=p2.next
            p1=p1.next
        return p1.data
        
l= LinkedList()
l.append(1)
l.append(2)
l.append(2)
l.append(7)
l.append(3)
l.append(9)
l.append(3)
print(l)

print(l.kth_element_from_last(7))