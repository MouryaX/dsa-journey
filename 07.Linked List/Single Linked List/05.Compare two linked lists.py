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
        
    def compare(self,head1,head2):
        h1=head1
        h2=head2
        
        while h1 and h2:
            if h1.data == h2.data:
                h1=h1.next
                h2=h2.next
            else:
                return 0
        if h1 is None and h2 is None:
            return 1
        return 0
    
ll1=LinkedList()
for i in range(1,6):
    ll1.insert(i)
    
ll2=LinkedList()
for i in range(1,6):
    ll2.insert(i)

ll1.display()
ll2.display()
print(ll1.compare(ll1.head, ll2.head))