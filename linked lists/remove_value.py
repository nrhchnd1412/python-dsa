class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    
def create_linked_list(li):
    head = Node(li[0])
    current = head
    for el in li[1:]:
        current.next= Node(el)
        current = current.next
    return head

def print_linked_list(head):
    value =[]
    current = head
    while current:
        value.append(current.value)
        current=current.next
    print(value)


def remove_value(li,value):
    dummy = Node(-1)
    dummy.next=li
    prev,current = dummy,li
    while current:
        if current.value==value:
            prev.next = current.next
        else:
            prev=current
        current=current.next
    return dummy.next

l1=create_linked_list([1,1,1,2,2,3,3,4])
print_linked_list(remove_value(l1,3))
