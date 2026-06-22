class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        
        while temp.next:
            temp = temp.next
            
        temp.next = new_node
        new_node.prev=temp
        
    def display(self):
        
        temp = self.head
        
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        
        print("None")
    
    def insertBeforeHead(self,X):
        if self.head is None:
            return Node(X)
        
        new_node = Node(X)
        self.head.prev=new_node
        new_node.next = self.head
        self.head=new_node  
    
    def del_head(self):
        if self.head is None:
            return 
        
        self.head=self.head.next
        if self.head:
            self.head.prev=None
    
    def rev(self):
        curr=self.head
        while curr:
            temp=curr.prev
            
l = LinkedList()
for i in range(10,50,10):
    l.add(i)
l.display() 
l.insertBeforeHead(9)
l.display()
l.del_head()
l.display()
        