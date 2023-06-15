class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class BST:
    def __init__(self) :
        self.root = None
    def inorder(self,root):
        if root: 
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)
    def insert(self,root, key):
        if root is None:
            return Node(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

root=BST();

root.insert(15);
root.insert(10);
root.insert(23);
root.insert(6);
root.insert(20);
root.insert(30);

