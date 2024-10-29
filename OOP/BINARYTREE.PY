class Node:
    data: int = None
    left_node = None
    right_node = None
    
    def __init__(self, data: int, left_node = None, right_node = None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        
    def search(self, query: int):
        if query < self.data: 
            if self.left_node is None:
                return None
            return self.left_node.search(query)
        elif query > self.data:
            if self.right_node is None:
                return None
            return self.right_node.search(query)
        else:
            return self
        
    def insert(self, data: int):
        if self.data:
            if data < self.data:
                if self.left_node is None:
                    self.left_node = Node(data)
                else: self.left_node.insert(data)
            elif data > self.data:
                if self.right_node is None:
                    self.right_node = Node(data)
                else:
                    self.right_node.insert(data)
    
class BinaryTree:
    root: Node = None
    
    def search(self, query: int):
        if self.root is None:
            return None
        
        if self.root.data == query:
            return self.root
        return self.root.search(query)
    
    def delete(self, query: int):
        element = self.search(query)
        if element is not None:
            element.data = None
            element.left_node = None
            element.right_node = None
    
    def insert(self, data: int):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data)
            