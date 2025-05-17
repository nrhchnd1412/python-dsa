from collections import deque

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Queue:
    def __init__(self):
        self.head=None
    
    def is_empty(self):
        return self.head==None
    
    def enque(self,data):
        node=Node(data)
        if not self.head:
            self.head=node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=node
            node.next=None
    
    def deque(self):
        if self.is_empty():
            return None
        item = self.head
        self.head=self.head.next
        return item.data


class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left_node=None
        self.right_node=None
    
def preorder_traversal(root_node):
    if not root_node:
        return None
    print(root_node.data)
    preorder_traversal(root_node.left_node)
    preorder_traversal(root_node.right_node)

def inorder_traversal(root_node):
    if not root_node:
        return None
    inorder_traversal(root_node.left_node)
    print(root_node.data)
    inorder_traversal(root_node.right_node)

def postorder_traversal(root_node):
    if not root_node:
        return None
    postorder_traversal(root_node.left_node)
    postorder_traversal(root_node.right_node)
    print(root_node.data)

def level_traversal(root_node):
    if not root_node:
        return
    # custom_queue=Queue()
    # custom_queue.enque(root_node)
    dq=deque()
    dq.append(root_node)
    while dq:
        item = dq.popleft()
        print(item.data)
        if item.left_node:
            dq.append(item.left_node)
        
        if item.right_node:
            dq.append(item.right_node)

def search(root_node,value):
    custom_queue=Queue()
    custom_queue.enque(root_node)
    while not (custom_queue.is_empty()):
        item = custom_queue.deque()
        if item.data.lower()==value.lower():
            return "Success"
        if item.left_node:
            custom_queue.enque(item.left_node)
        if item.right_node:
            custom_queue.enque(item.right_node)
        
    return "Doesn't exist"

def insert_node(root_node,value):
    new_node=TreeNode(value)
    if not root_node:
        root_node=new_node
        return
    custom_queue=Queue()
    custom_queue.enque(root_node)
    while not custom_queue.is_empty():
        item = custom_queue.deque()
        if item.left_node:
            custom_queue.enque(item.left_node)
        else:
            item.left_node=new_node
            return
        if item.right_node:
            custom_queue.enque(item.right_node)
        else:
            item.right_node=new_node
            return
    pritn('inserted')

def find_deepest_node(root_node):
    custom_queue=Queue()
    custom_queue.enque(root_node)
    while not (custom_queue.is_empty()):
        item = custom_queue.deque()
        if item.left_node:
            custom_queue.enque(item.left_node)
        if item.right_node:
            custom_queue.enque(item.right_node)
    return item

def delete_node(root_node,value):
    if not root_node:
        return None
    target_node=None
    parent_node=None
    custom_queue=Queue()
    custom_queue.enque(root_node)

    # find target and parent node
    while not custom_queue.is_empty():
        item=custom_queue.deque()
        if item.data==value:
            target_node=item
            break
        if item.left_node and item.left_node.data==value:
            parent_node=item
            target_node=item.left_node
            break
        if item.right_node and item.right_node.data==value:
            parent_node=item
            target_node=item.right_node
            break
        if item.left_node:
            custom_queue.enque(item.left_node)
        if item.right_node:
            custom_queue.enque(item.right_node)
    if not target_node:
        print('target item not found')
        return None
    
    # find deepest node
    deepest_node = find_deepest_node(root_node)
    if target_node is deepest_node:
        if parent_node:
            if parent_node.left_node is target_node:
                parent_node.left_node=None
            else:
                parent_node.right_node=None
        else:
            root_node=None
        return None
    target_node.data=deepest_node.data

    # delete deepest node
    custom_queue=Queue()
    custom_queue.enque(root_node)
    while not custom_queue.is_empty():
        item=custom_queue.deque()
        if item.left_node==deepest_node:
            item.left_node=None
        elif item.right_node==deepest_node:
            item.right_node=None
        if item.left_node:
            custom_queue.enque(item.left_node)
        if item.right_node:
            custom_queue.enque(item.right_node)

root_node = TreeNode("Drinks")
hot_node=TreeNode("Hot")
cold_node=TreeNode("Cold")

tea_node= TreeNode("Tea")
coffee_node= TreeNode("Coffee")

cola_node=TreeNode("Cola")
fanta_node=TreeNode("Fanta")

root_node.left_node=hot_node
root_node.right_node=cold_node
hot_node.left_node=tea_node
hot_node.right_node=coffee_node
cold_node.left_node=cola_node
cold_node.right_node=fanta_node

print('Preorder traversal')
print('====================')
preorder_traversal(root_node)
print('\n')
print('Inorder traversal')
print('====================')
inorder_traversal(root_node)
print('\n')
print('Postorder traversal')
print('====================')
postorder_traversal(root_node)
print('\n')
print('Levelorder traversal')
print('====================')
level_traversal(root_node)
print('\n')
print('Searching item')
print('====================')
print(search(root_node,"Cola"))
print('\n')
print('Inserting item')
print('====================')
insert_node(root_node,"Ginger")
level_traversal(root_node)
print('Printing deepest node')
print('====================')
print(find_deepest_node(root_node).data)
print('\n')
print('deleting node')
print('====================')
print(delete_node(root_node,"Tea"))
level_traversal(root_node)


