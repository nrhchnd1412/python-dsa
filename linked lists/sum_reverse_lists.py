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

def sum_reverse(l1,l2):
    n1 = l1.head
    n2=l2.head
    carry = 0
    output = LinkedList()

    while n1 or n2:
        result=carry
        if n1:
            result+=n1.data
            n1=n1.next
        if n2:
            result+=n2.data
            n2=n2.next
        output.append(int(result%10))
        carry=result/10
    return output

l1= LinkedList()
l1.append(2)
l1.append(1)
l1.append(3)

l2= LinkedList()
l2.append(4)
l2.append(5)
l2.append(6)

summed = sum_reverse(l1,l2)
print(summed)

