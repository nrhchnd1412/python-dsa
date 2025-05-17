from collections import deque

class Node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root_node=None
    
    def insert(self,value):
        self.root_node=self._insert_recursive(self.root_node,value)
    
    def _insert_recursive(self,root,value):
        if not root:
            return Node(value)
        if root.data>value:
            root.left = self._insert_recursive(root.left,value)
        elif root.data<value:
            root.right=self._insert_recursive(root.right,value)
        return root
    
    def level_traverse(self):
        if not self.root_node:
            return
        q=deque()
        q.append(self.root_node)
        while q:
            item=q.popleft()
            print(item.data)
            if item.left:
                q.append(item.left)
            if item.right:
                q.append(item.right)
    
    def _find_minimum(self,root):
        if not root:
            return None
        temp=root
        while temp.left:
            temp=temp.left
        return temp
    
    def delete(self,value):
        self.root_node=self._delete_recursive(self.root_node,value)
    
    def _delete_recursive(self,root,value):
        if not root:
            return None
        if root.data>value:
            root.left=self._delete_recursive(root.left,value)
        elif root.data<value:
            root.right=self._delete_recursive(root.right,value)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            root.key=self._find_minimum(root.right)
            root.right=self._delete_recursive(root.right,root.key)
        return root
    
    def search(self,value):
        return self._search_recursively(self.root_node,value)

    def _search_recursively(self,root,value):
        if root is None or root.data==value:
            return root
        if root.data>value:
            return self._search_recursively(root.left,value)
        elif root.data<value:
            return self._search_recursively(root.right,value)

    def contains(self,value):
        return self._search_recursively(self.root_node,value) is not None
    
        
b=BST()
b.insert(30)
b.delete(30)
b.level_traverse()
# b.insert(10)
# b.insert(20)
# b.insert(40)
# b.insert(70)
# b.insert(90)
# b.insert(10)
# b.insert(25)
# b.level_traverse()


# print("\nAfter deletion")
# b.delete(40)
# b.level_traverse()
# print("\nSearch")
# print(b.search(90).data)
# print("\nCheck contains")
# print(b.contains(90))


            
