class Node(object):
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def _init_(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        newnode=Node(new_val)
        if self.root==None:
            self.root=newnode
        else:
            current=self.root
            parent=self.root
            while(current!=None):
                parent=current
                if(new_val<current.value):
                    current=current.left
                else:
                    current=current.right
            if(new_val<parent.value):
                parent.left=newnode
            parent.right=newnode

    def printSelf(self):
        # Your code goes here
        print(self.root)

    def search(self, find_val):
        # Your code goes here
        while(self.root!=None):
            if self.root.value==find_val:
                return True
            if self.root.value>find_val:
                self.root=self.root.left
            self.root=self.root.right
        return False