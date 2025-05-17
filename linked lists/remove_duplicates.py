class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def reverse(self):
        prev_node=None
        current_node=self.head
        while current_node!=None:
            next_node=current_node.next
            current_node.next=prev_node
            prev_node=current_node
            current_node=next_node
        self.head,self.tail=self.tail,self.head

    def find_middle(self):
        n = self.length //2
        temp = self.head
        for _ in range(n):
            temp = temp.next
        print(temp.value)

    def find_middle_fast_slow_pointer(self):
        fast= self.head
        slow=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast= fast.next.next
        print(slow.value)

    def remove_duplicates(self):
        node_values = set()
        current_node=self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:
                current_node.next=current_node.next.next
                self.length-=1
            else:
                node_values.add(current_node.next.value)
                current_node=current_node.next
            self.tail=current_node

l = LinkedList()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.append(10)
print(l)
l.find_middle_fast_slow_pointer()
# l.reverse()
l.remove_duplicates()
print(l)