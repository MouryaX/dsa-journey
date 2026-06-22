class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head=new_node
            return
        
        temp = self.head
        while temp.next:
            temp=temp.next
            
        temp.next = new_node
    
    def display(self):
        temp = self.head
        length=0
        while temp:
            print(temp.data,end="-->")
            length+=1
            temp=temp.next
        print("None")
        print("Length:",length)
    
    def insert_at_beg(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node   #This is not required here 
            return
        
        new_node.next = self.head
        self.head=new_node
        
    def del_head(self):
        if self.head is None:
            return
        temp=self.head
        self.head=temp.next
    
    def del_tail(self):
        if self.head is None or self.head.next is None:
            return
        
        temp=self.head
        while temp.next.next:
            temp=temp.next
            
        temp.next=None
    
    def del_spec(self,node):
        if self.head.next is None:
            self.head = None
            return
        temp=self.head
        while temp.next.data != node:
            temp=temp.next
        temp.next=temp.next.next
        
    def search_node(self,node):
        temp=self.head
        
        while temp:
            if temp.data == node:
                return True
            
            temp=temp.next
        return False
        
l =LinkedList()
l.insert(0)
l.insert(1)
l.insert(2)
l.insert_at_beg(5)
l.display()
l.del_spec(1)
l.display()
print(l.search_node(2))