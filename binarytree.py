class Node:
    def __init__(self, data:int):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def add(self,data:int):
        self.root = self.recur_Add(self.root,data)
    
    def recur_Add(self,node:Node,data:int):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self.recur_Add(node.left, data)
        if data > node.data:
            node.right = self.recur_Add(node.right, data)
        return node
    
    def printTree(self):
        self.recur_Print(self.root)
            
    def recur_Print(self, node: Node, level=0, prefix="Root: "):
        if node is not None:
            print("    " * level + prefix + str(node.data))
            if node.left or node.right:
                if node.left:
                    self.recur_Print(node.left, level + 1, "L--> ")
                else:
                    print("    " * (level + 1) + "L--> None")
                
                if node.right:
                    self.recur_Print(node.right, level + 1, "R--> ")
                else:
                    print("    " * (level + 1) + "R--> None")


tree = BinaryTree()
tree.add(8)
tree.add(3)
tree.add(10)
tree.add(1)
tree.add(6)
tree.add(14)
tree.add(4)
tree.add(7)
tree.add(13)
tree.printTree()  # Output: 8