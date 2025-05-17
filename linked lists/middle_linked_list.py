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

def find_middle(l_head):
    slow = l_head
    fast= l_head
    while fast and fast.next:
        slow=slow.next
        fast = fast.next.next
    return slow.value

li = create_linked_list([1,2,1,5])
print(find_middle(li))