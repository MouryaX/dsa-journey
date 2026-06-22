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
        
    def removeDuplicates(self,llist):
        if llist is None:
            return llist
            
        t=llist
        while t and t.next:
            if t.data == t.next.data:
                t.next = t.next.next
            else:
                t=t.next
        return llist
    
ll1=LinkedList()
for i in range(1,6):
    ll1.insert(i)
    ll1.insert(i+1)
    ll1.insert(i+1)
ll1.display()
print("--------After Removing Duplicates--------")
ll1.removeDuplicates(ll1.head)
ll1.display()