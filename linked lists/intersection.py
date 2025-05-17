class Node:
    def __init__(self,value,next=None):
        self.data=value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __len__(self):
        if not self.head:
            return 0
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count

    def append(self,value):
        node=Node(value)
        if not self.head:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            node.next=None
            self.tail=node
    
    def __str__(self):
        result=""
        temp=self.head
        while temp:
            result+=str(temp.data)
            temp=temp.next
            if not temp:
                break
            result+="->"
        return result
    
    def chain(self,node):
        self.tail.next=node
        self.tail=node
    
    def find_intersection(self,l2):
        if self.tail!=l2.tail:
            return False
        length_1=len(self)
        length_2=len(l2)

        shorter=self if length_1<length_2 else l2
        longer = l2 if length_2>length_1 else self

        diff = len(longer)-len(shorter)
        longer_node=longer.head
        shorter_node=shorter.head
        for _ in range(diff):
            longer_node=longer_node.next
        
        while shorter_node is not longer_node:
            shorter_node=shorter_node.next
            longer_node=longer_node.next
        return shorter_node.data
        

l1=LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)

l2=LinkedList()
l2.append(10)
l2.append(11)
l2.append(12)

new_node1=Node(81)
new_node2=Node(91)
new_node3=Node(101)
new_node1.next=new_node2
new_node2.next=new_node3
new_node3.next=None

l1.chain(new_node1)
l2.chain(new_node1)

print(l1,len(l1))
print(l2,len(l2))

print(l1.find_intersection(l2))