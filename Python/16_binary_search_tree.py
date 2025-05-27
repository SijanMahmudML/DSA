"""Binary Search Tree using Linked List"""

class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        elif data<root.item:
            root.left=self.rinsert(root.left,data)
        elif data>root.item:
            root.right=self.rinsert(root.right,data)
        return root
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root is None or root.item==data:
            return root
        elif data < root.item:
            return self.rsearch(root.left,data)
        elif data > root.item:
            return self.rsearch(root.right,data)
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)
    def min(self,temp):
        current=temp
        while current.left is not None:
            current=current.left
        return current.item
    def max(self,temp):
        current=temp
        while current.right is not None:
            current=current.right
        return current.item
    def delete(self,data):
        self.root=self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None:
            return root
        elif data < root.item:
            root.left=self.rdelete(root.left,data)
        elif data > root.item:
            root.right = self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                root.item=self.min(root.right)
                self.rdelete(self.min(root.right))
        return root
    def size(self):
        return len(self.inorder())
        
            
        

        

"""Driver Code"""

b1=BST()
b1.insert(50)
b1.insert(30)
b1.insert(80)
b1.insert(10)
b1.insert(40)
b1.insert(70)
b1.insert(100)
b1.insert(35)
b1.insert(60)
b1.insert(75)
b1.insert(90)
b1.insert(55)
b1.insert(110)

print(b1.inorder())
print(b1.preorder())
print(b1.postorder())
print(b1.min(b1.root))
print(b1.max(b1.root))
print(b1.size())

b1.delete(10)
b1.delete(30)
b1.delete(55)

print(b1.inorder())
print(b1.preorder())
print(b1.postorder())
print(b1.min(b1.root))
print(b1.max(b1.root))
print(b1.size())
