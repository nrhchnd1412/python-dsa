'''
Write an algorithm to find the next node (i.e in-order successor) of given node in a binary search tree. 
You may assume that each node has a link to its parent.
'''


class TreeNode:
    def __init__(self,value,parent=None):
        self.value=value
        self.left=None
        self.right=None
        self.parent=parent

class BST:
    def __init__(self):
        self.root_node=None
    
    def insert(self,value):
        if not self.root_node:
            self.root_node=TreeNode(value)
        else:
            self._insert(self.root_node,value)

    def _insert(self,node,value):
        if node.value>=value:
            if node.left is None:
                node.left=TreeNode(value,node)
            else:
                self._insert(node.left,value)
        else:
            if node.right is None:
                node.right=TreeNode(value,node)
            else:
                self._insert(node.right,value)

    def find(self,value):
        return self._find(self.root_node,value)

    def _find(self,node,value):
        if node is None or node.value==value:
            return node
        if node.value>=value:
            return self._find(node.left,value)
        else:
            return self._find(node.right,value)
        
    def inorder_successor(self,value):
        node = self.find(value)
        if not node:
            return None
        # case 1 -- if node.right exists, find the leftmost element in the right subtree
        if node.right:
            current = node.right
            while current.left:
                current=current.left
            return current

        # case 2 -- if no right child, then go up in the parent hierarchy until u find a node which is left
        # its parent. The parent will be the successor

        curr= node
        while curr.parent and curr==curr.parent.right:
            curr=curr.parent
        return curr.parent

    def inorder_traversal(self):
        self._inorder_traversal(self.root_node)
    
    def _inorder_traversal(self,node):
        if not node:
            return None
        self._inorder_traversal(node.left)
        print(node.value)
        self._inorder_traversal(node.right)
        

def print_tree(node, prefix="", is_left=True):
    if node is not None:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

bst=BST()
bst.insert(10)
bst.insert(15)
bst.insert(5)
bst.insert(8)
bst.insert(17)
bst.insert(14)

print_tree(bst.root_node)

found = bst.find(170)
print(bool(found))

successor=bst.inorder_successor(14)
if successor:
    print(successor.value)
else:
    print('no successor')

#bst.inorder_traversal()