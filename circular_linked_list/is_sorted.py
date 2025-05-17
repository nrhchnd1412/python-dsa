class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(nodes))

    def is_sorted(self):
        if not self.head:
            return True
        if self.head.next == self.head:
            return True
        prev = self.head
        current = self.head.next
        while True:
            if not prev.data<=current.data:
                return False
            prev=current
            current=current.next
            if current==self.head:
                return True

c = CircularLinkedList()
c.append(10)
c.append(20)
c.append(9)

print(c.is_sorted())