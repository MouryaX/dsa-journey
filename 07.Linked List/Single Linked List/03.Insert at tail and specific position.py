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
        
    def insertNodeAtTail(self, data):
        new_node = Node(data)

        if self.head is None:
            return new_node

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        return self.head
    
    def display(self):
        
        temp = self.head
        
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        
        print("None")
    
    def insert_at_spec(self,data,pos):
        new_node=Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return self.head
        
        temp=self.head
        for _ in range(pos-1):
            temp=temp.next
        new_node.next = temp.next
        temp.next = new_node
        return self.head
        
    
ll=LinkedList()

for i in range(1,6):
    ll.insert(i)
ll.display()
head=ll.head
ll.insertNodeAtTail(6)
ll.insert_at_spec("Mourya",1)
ll.display()