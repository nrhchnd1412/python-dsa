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

def check_palindrome(l_head):
    fast= l_head
    slow=l_head
    while fast and fast.next:
        slow=slow.next
        fast = fast.next.next
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev= slow
        slow=nxt
    while prev:
        if l_head.value!=prev.value:
            return False
        prev=prev.next
        l_head=l_head.next
    return True

li =create_linked_list([1,2,1])
print(check_palindrome(li))