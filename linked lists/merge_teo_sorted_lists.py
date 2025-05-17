class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

def create_linked_lists(li):
    head = Node(li[0])
    current =head
    for i in li[1:]:
        current.next = Node(i)
        current = current.next
    return head

def print_linked_list(head):
    value =[]
    current = head
    while current:
        value.append(current.value)
        current=current.next
    print(value)

def merged_linked_lists(l1_head,l2_head):
    dummy = Node(-1)
    current = dummy
    while l1_head and l2_head:
        if l1_head.value <= l2_head.value:
            current.next=l1_head
            l1_head=l1_head.next
        else:
            current.next=l2_head
            l2_head=l2_head.next
        current=current.next
    if l1_head:
        current.next=l1_head
    elif l2_head:
        current.next=l2_head
    return dummy.next

l1_head = create_linked_lists([1,2,3,4])
l2_head = create_linked_lists([2,3,3,4])

merged_head = merged_linked_lists(l1_head,l2_head)
print_linked_list(merged_head)