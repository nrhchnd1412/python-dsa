from collections import deque

class AVLNode:
    def __init__(self,value=None):
        self.data=value
        self.height=1
        self.left=None
        self.right=None

class AVLTree:
    def __init__(self):
        self.root_node=None

    def height(self,node):
        if not node:
            return 0
        return node.height
    
    def balance_factor(self,node):
        if not node:
            return 0
        return self.height(node.left)-self.height(node.right)

    def update_height(self,node):
        if not node:
            return
        node.height = 1+max(self.height(node.left),self.height(node.right))

    def rotate_right(self,node):
        new_root=node.left
        temp_node=new_root.right
        node.left=temp_node
        new_root.right=node

        self.update_height(node)
        self.update_height(new_root)
        return new_root
    
    def rotate_left(self,node):
        new_root=node.right
        temp_node=new_root.left
        node.right=temp_node
        new_root.left=node
        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def insert(self,value):
        self.root_node=self._insert_recursively(self.root_node,value)

    def _insert_recursively(self,node,value):
        if node is None:
            return AVLNode(value)
        if node.data>value:
            node.left=self._insert_recursively(node.left,value)
        elif node.data<value:
            node.right=self._insert_recursively(node.right,value)
        else:
            return node
        self.update_height(node)
        balance_factor=self.balance_factor(node)
        
        ## left heavy
        if balance_factor>1:
            ##left left
            if self.balance_factor(node.left)>=0:
                return self.rotate_right(node)
            ## left right
            elif self.balance_factor(node.left)<0:
                node.left=self.rotate_left(node.left)
                return self.rotate_right(node)
        ## right heavy
        elif balance_factor<-1:
            ## right right
            if self.balance_factor(node.right)<=0:
                return self.rotate_left(node)
            ## right left
            elif self.balance_factor(node.right)>0:
                node.right=self.rotate_right(node.right)
                return self.rotate_left(node)
        return node

    def search(self,value):
        return self._search_recursive(self.root_node,value)
    
    def contains(self,value):
        return self._search_recursive(self.root_node,value) is not None
    
    def _search_recursive(self,node,value):
        if not node or node.data==value:
            return node
        if node.data>value:
            return self._search_recursive(node.left,value)
        else:
            return self._search_recursive(node.right,value)
    
    def find_minimum(self,node):
        temp=node
        while temp.left:
            temp=temp.left
        return temp
    
    def delete(self,value):
        self.root_node=self._delete_recursive(self.root_node,value)

    def _delete_recursive(self,node,value):
        if not node:
            return None
        if node.data>value:
            node.left=self._delete_recursive(node.left,value)
        elif node.data<value:
            node.right=self._delete_recursive(node.right,value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            node.key=self.find_minimum(node.right)
            node.right=self._delete_recursive(node.right,node.key)
        
        self.update_height(node)
        balance_factor=self.balance_factor(node)

        ## left heavy
        if balance_factor>1:
            ##left left
            if self.balance_factor(node.left)>=0:
                return self.rotate_right(node)
            ## left right
            elif self.balance_factor(node.left)<0:
                node.left=self.rotate_left(node.left)
                return self.rotate_right(node)
        ## right heavy
        elif balance_factor<-1:
            ## right right
            if self.balance_factor(node.right)<=0:
                return self.rotate_left(node)
            ## right left
            elif self.balance_factor(node.right)>0:
                node.right=self.rotate_right(node.right)
                return self.rotate_left(node)
        
        return node

    def level_traversal(self):
        q=deque()
        q.append(self.root_node)
        while q:
            item=q.popleft()
            print(item.data)
            if item.left:
                q.append(item.left)
            if item.right:
                q.append(item.right)

avl=AVLTree()
avl.insert(100)
avl.insert(50)
avl.insert(150)
avl.insert(30)
avl.insert(40)
avl.insert(110)
avl.insert(160)
avl.insert(168)
avl.insert(170)

avl.delete(110)
avl.level_traversal()