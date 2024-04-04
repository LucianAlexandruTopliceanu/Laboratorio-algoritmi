class Dizionario_ABR:

    def __init__(self):
        self.root=None

    def insert(self,key,value):
        z=_Node(key,value)
        y=None
        x=self.root
        while x!= None:
            y=x
            if z.key<x.key:
                x=x.left
            else:
                x=x.right
        z.p=y
        if y== None:
            self.root=z     
        elif z.key<y.key:
            y.left=z
        else:
            y.right=z
    
    def search(self,key):
        x=self.root
        while x!=None and key!=x.key:
            if key<x.key:
                x=x.left
            else:
                x=x.right
        return x
    
    def delete(self,key):
        z=self.search(key)
        if z==None:
            return
        if z.left==None:
            self._transplant(z,z.right)
        elif z.right==None:
            self._transplant(z,z.left)
        else:
            y=self._minimum(z.right)
            if y.p!=z:
                self._transplant(y,y.right)
                y.right=z.right
                y.right.p=y
            self._transplant(z,y)
            y.left=z.left
            y.left.p=y

    def size(self):
        x=self.root
        count=0
        count=self._inorder_count(x,count)
        return count
    
    def _inorder_count(self,x,count):
        if x is not None:
            count=count+1
            count=self._inorder_count(x.left,count)
            count=self._inorder_count(x.right,count)
        return count
            
    def _transplant(self,u,v):
        if u.p==None:
            self.root=v
        elif u==u.p.left:
            u.p.left=v
        else:
            u.p.right=v
        if v!=None:
            v.p=u.p

    def _minimum(self,x):
        while x.left!=None:
            x=x.left
        return x

class _Node:

    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
        self.p=None