class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
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
        
    def display(self):
        
        temp = self.head
        
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        
        print("None")
                
l = LinkedList()
l.add(10)
l.add(20)
l.add(30)
l.display()

        