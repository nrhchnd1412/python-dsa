class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.data)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node


    def insert_into_sorted(self, data):
        if not self.head:
            return None

        if self.head ==self.head.next:
            # prepend scenario
            if data<=self.head.data:
                self.prepend(data)
                return
            else:
                # append scenario
                self.append(data)
                return
        if self.head.data>=data:
            self.prepend(data)
            return
        node = Node(data)
        prev = self.head
        current = self.head.next
        while current!=self.head:
            if node.data<=current.data:
                prev.next = node
                node.next = current
                break
            elif current.next == self.head:
                self.append(node.data)
                break
            else:
                prev = current
            current=current.next


c= CircularLinkedList()
c.append(10)

print(c)
print('Inserting into sorted CLL')
c.insert_into_sorted(5)
print(c)