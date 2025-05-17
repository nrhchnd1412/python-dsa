class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def split(self):
        if not self.head:
            return None
        if self.head.next == self.head:
            return (self.head,None)
        slow=self.head
        fast=self.head

        # slow and fast pointer approach
        while fast.next!=self.head or fast.next.next != self.head:
            fast= fast.next.next
            slow=slow.next
        
        # case where there are even number of nodes
        if fast.next.next==self.head:
            fast=fast.next
        
        head2 = slow.next
        fast.next= head2

        slow.next = self.head

        return self.head,head2
    
c = CSLinkedList()
c.append(10)
c.append(20)
c.append(30)
c.append(40)
print(c.split())