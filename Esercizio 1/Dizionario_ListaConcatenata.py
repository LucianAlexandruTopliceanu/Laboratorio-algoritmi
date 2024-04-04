
class Dizionario_ListaConcatenata :
    head=None

    def insert (self,key,value):
        x=_Node(key,value)
        x.next=self.head
        if self.head != None:
            self.head.prev=x
        self.head=x
        x.prev=None
    
    def search(self,key):
        x=self.head
        while x!=None and x.key!=key:
            x=x.next
        return x

    def delete(self,key):
        x=self.search(key)
        if x==None:
            return
        if x.prev!=None:
            x.prev.next=x.next
        else: self.head=x.next
        if x.next!=None:
            x.next.prev=x.prev

    def size(self):
        count=0
        x=self.head
        while x is not None:
            count=count+1
            x=x.next
        return count
    
class _Node :

    def __init__(self,key,value) :
        self.key=key
        self.value=value
        self.next=None
        self.prev=None