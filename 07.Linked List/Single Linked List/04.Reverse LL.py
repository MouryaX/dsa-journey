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
        
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        
        print("None")
    
    def rev(self):
        if self.head is None:
            return
        temp=self.head
        prev=None
        while temp:
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=nxt
        
        while prev:
            print(prev.data,end="->")
            prev=prev.next
        print("None")
    
ll=LinkedList()
for i in range(1,6):
    ll.insert(i)
ll.display()
ll.rev()