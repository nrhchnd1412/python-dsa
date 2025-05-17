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
    
    def delete_by_value(self, target):
        if not self.head:
            return
        
        #only one node and that contains the target value
        if self.head.value==target and self.head.next == self.head:
            self.head=None
            return
        
        #case where target is present in head node(s)
        while self.head and self.head.value == target:
            self.head = self.head.next
            self.tail.next = self.head
            if self.head==self.tail and self.head.value == target:
                self.head = None
                self.tail=None
                return
        
        #handle rest cases
        while True:
            current = self.head
            prev = current
            current=current.next
            while current!= self.head:
                if current.value == target:
                    prev.next = current.next
                else:
                    prev = current
                current=current.next
            break
            


c = CSLinkedList()
c.append(10)
c.append(5)
c.append(6)

print(c)

c.delete_by_value(6)
print(c)