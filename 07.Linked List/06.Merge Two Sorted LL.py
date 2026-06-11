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
        
    def merge(self,head1,head2):
        h1=head1
        h2=head2
        
        d = Node(0)
        tail = d
        
        while h1 and h2:
            if h1.data <= h2.data:
                tail.next = h1
                h1=h1.next
            else:
                tail.next=h2
                h2=h2.next
                
            tail=tail.next 
        if h1:
            tail.next=h1
        if h2:
            tail.next=h2 
        
        self.head=d.next
        self.display()
    
ll1=LinkedList()
for i in range(1,6):
    ll1.insert(i)
    
ll2=LinkedList()
for i in range(1,4):
    ll2.insert(i)

ll1.display()
ll2.display()
ll1.merge(ll1.head, ll2.head)