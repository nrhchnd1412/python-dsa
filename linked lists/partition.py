class Node:
    def __init__(self,value,next=None):
        self.data=value
        self.next=next

    def __str__(self):
        result =''
        while True:
            result+=str(self.data)
            self = self.next
            if self==None:
                break
            result+="->"
        return result

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

    def partition(self,k):
        if not self.head:
            return None
        less_l = Node(-1)
        greater_l = Node(-1)

        less = less_l
        greater = greater_l

        original = self.head
        while original:
            if original.data <=k:
                print(f'original data less or equal {original.data}')
                less.next= original
                less=less.next
            else:
                print(f'original data greater  {original.data}')
                greater.next= original
                greater=greater.next
            original=original.next
        greater.next=None
        less.next= greater_l.next
        self.head= less_l.next

l= LinkedList()
l.append(20)
l.append(1)
l.append(5)
l.append(8)
l.append(15)
l.append(1)
l.append(2)
l.append(17)
l.append(13)
print(l)

l.partition(17)
print(l)