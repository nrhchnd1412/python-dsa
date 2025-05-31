'''
Implement a function to check if a binary tree is balanced. For the purposes of this question, 
a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ
by more than one.
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

def is_tree_balanced(root):
    def check(node):
        if not node:
            return 0,True
        left_height,left_balanced=check(node.left)
        right_height,right_balanced=check(node.right)
        current_height=1+max(left_height,right_height)
        is_current_balanced= (
            left_balanced and right_balanced and abs(left_height-right_height)<=1
        )
        return current_height,is_current_balanced
    _,is_balanced=check(root)
    return is_balanced
    

bst = BST(10)
bst.insert(1)
bst.insert(5)
bst.insert(11)
bst.insert(15)
bst.insert(9)

print_tree(bst.root_node)
print(is_tree_balanced(bst.root_node))