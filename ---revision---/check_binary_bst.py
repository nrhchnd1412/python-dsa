'''
Implement a function to check if a binary tree is a Binary Search Tree.

Time complexity: O(n)
'''

class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def is_valid_bst(root_node):
    def check(node,min_value=float("-inf"),max_value=float("inf")):
        if not node:
            return True
        if not (min_value<node.value<max_value):
            return False
        # Recursively validate left and right subtrees with updated ranges
        return (check(node.left,min_value,node.value) and
                check(node.right,node.value,max_value)
            )
    return check(root_node)
    
# Construct a valid BST
root = TreeNode(10,
         left=TreeNode(5,
               left=TreeNode(2),
               right=TreeNode(7)),
         right=TreeNode(15,
                left=TreeNode(12),
                right=TreeNode(20)))

print(is_valid_bst(root))  # Output: True

# Construct an invalid BST
invalid_root = TreeNode(10,
                left=TreeNode(5,
                      right=TreeNode(12)))  # 12 is invalid in left subtree

print(is_valid_bst(invalid_root))  # Output: False