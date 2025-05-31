'''
Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth
(ie , if you have a tree with depth D, you’ll have D linked lists)
'''

from collections import deque

class BstNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class ListNode:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next

class BST:
    def __init__(self,root_node_value):
        self.root_node=BstNode(root_node_value)
    
    def insert(self,value,root=None):
        if not root:
            root=self.root_node
        if root.value>=value:
            if not root.left:
                root.left=BstNode(value)
            else:
                self.insert(value,root.left)
        else:
            if not root.right:
                root.right=BstNode(value)
            else:
                self.insert(value,root.right)

def print_tree(node, prefix="", is_left=True):
    if node is not None:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

def level_of_depth(root_node):
    if not root_node:
        return None
    results=[]
    q=deque([root_node])
    while q:
        li_node=ListNode()
        current=li_node
        level_length=len(q)
        for _ in range(level_length):
            item=q.popleft()
            current.next=ListNode(item.value)
            current=current.next
            if item.left:
                q.append(item.left)
            if item.right:
                q.append(item.right)
        results.append(li_node.next)
    return results

def print_level_depths(results):
    for item in results:
        while item:
            print(f'{item.value}', end=" ")
            item=item.next
            if item:
                print(" -> ",end="")
            else:
                break
        print('\n')

bst = BST(10)
bst.insert(1)
bst.insert(5)
bst.insert(11)
bst.insert(15)
bst.insert(9)

print_tree(bst.root_node)
results=level_of_depth(bst.root_node)
print_level_depths(results)