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
    
ll=LinkedList()

for i in range(1,6):
    ll.insert(i)
ll.display()
head=ll.head
ll.insertNodeAtTail(6)
ll.display()