'''
Design an algorithm and write code to find the first common ancestor of two 
nodes in a binary tree. Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.
'''

class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def find_common_ancestor(root,p,q):
    if not root:
        return None
    if root==p or root==q:
        return root
    left=find_common_ancestor(root.left,p,q)
    right=find_common_ancestor(root.right,p,q)

    if left and right:
        return root
    return left if left else right

A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')

A.left = B
A.right = C
B.left = D
B.right = E
C.right = F

ancestor = find_common_ancestor(A, D, E)
print("Common Ancestor of D and E:", ancestor.value)  # Output: B

root = TreeNode(55)

root.left = TreeNode(44)
root.right = TreeNode(77)

root.left.left = TreeNode(22)
root.left.right = TreeNode(99)

root.left.left.left = TreeNode(35)
n_88=TreeNode(88)
root.left.left.right = n_88

root.left.right.left = TreeNode(90)
root.left.right.right = TreeNode(95)
n_33=TreeNode(33)
root.left.right.left.left = n_33


ancestor = find_common_ancestor(root, n_33, n_88)
print(ancestor.value)