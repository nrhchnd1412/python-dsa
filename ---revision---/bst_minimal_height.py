'''
from a given sorted (asc) order of unique integers, create a BST such that it
has minimum height
'''


from collections import deque

class BSTNode:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

class BST:
    def __init__(self,root_node_value):
        self.root_node=BSTNode(root_node_value)

    def insert(self,value,root=None):
        if not root:
            root=self.root_node
        if value<=root.value:
            if not root.left:
                root.left=BSTNode(value)
            else:
                self.insert(value,root.left)
        else:
            if not root.right:
                root.right=BSTNode(value)
            else:
                self.insert(value,root.right)
    
    def traverse(self):
        if not self.root_node:
            return []
        q=deque([self.root_node])
        while q:
            item = q.popleft()
            print(item.value)
            if item.left:
                q.append(item.left)
            if item.right:
                q.append(item.right)

class MinHeightBst:
    def insert(self,arr):
        if not arr:
            return None
        arr_mid=len(arr)//2
        root=BSTNode(arr[arr_mid])
        root.left= self.insert(arr[:arr_mid])
        root.right=self.insert(arr[arr_mid+1:])
        return root


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

#bst.traverse()
#print_tree(bst.root_node)
            
sortedArray = [1,2,3,4,5,6,7,8,9]
min_bst= MinHeightBst()
root = min_bst.insert(sortedArray)
print_tree(root)
print(is_tree_balanced(root))