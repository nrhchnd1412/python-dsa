'''
Write an algorithm to find the next node (i.e in-order successor) of given node in a binary search tree. 
You may assume that each node has a link to its parent.
'''

class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

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
            if not node.left:
                node.left=TreeNode(value)
            else:
                self._insert(node.left,value)
        else:
            if not node.right:
                node.right=TreeNode(value)
            else:
                self._insert(node.right,value)
    
    def find(self,value):
        return self._find(self.root_node,value)
    
    def _find(self,node,value):
        if not node or node.value==value:
            return node
        if node.value>=value:
            return self._find(node.left,value)
        else:
            return self._find(node.right,value)

    def inorder_successor(self,value):
        node= self.find(value)

        # case 1- if there is a right child of node
        if node:
            if node.right:
                successor=node.right
                while successor.left:
                    successor=successor.left
                return successor
            
            successor=None
            current=self.root_node
            while current:
                if current.value>value:
                    successor=current
                    current=current.left
                elif current.value<value:
                    current=current.right
                else:
                    break
            return successor

bst=BST()
bst.insert(10)
bst.insert(15)
bst.insert(5)
bst.insert(8)
bst.insert(17)
bst.insert(14)

found = bst.find(170)
print(bool(found))

successor=bst.inorder_successor(14)
if successor:
    print(successor.value)
else:
    print('no successor')