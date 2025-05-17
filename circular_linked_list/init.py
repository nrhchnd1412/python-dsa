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
        result = ''
        current = self.head
        while True:
            result +=str(current.value)
            current=current.next
            if current==self.head:
                break
            result+="->"
        return result
    
    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
            node.next=node
        else:
            self.tail.next =node
            node.next=self.head
            self.tail=node
        self.length+=1
    
    def prepend(self, value):
        node = Node(value)
        if not self.head:
            self.head=node
            self.tail=node
            node.next = node
        else:
            node.next=self.head
            self.head=node
            self.tail.next = self.head
        self.length+=1
    
    def delete_cl(self):
        # Cascade delete
        self.head=self.tail=None


c = CSLinkedList()
c.append(10)
c.append(20)
c.append(30)
c.prepend(800)
print(f'{c.length=}')
print(c)