class BST:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

def insert(root_node,value):
    if not root_node.data:
        root_node.data=value
        root_node.left=None
        root_node.right=None
    else:
        if root_node.data>=value:
            if not root_node.left:
                root_node.left=BST(value)
            else:
                insert(root_node.left,value)
        else:
            if not root_node.right:
                root_node.right=BST(value)
            else:
                insert(root_node.right,value)
    print('Node added to BST')

bst = BST()
insert(bst,70)
insert(bst,60)
insert(bst,80)

print(bst.left.data)
print(bst.right.data)
