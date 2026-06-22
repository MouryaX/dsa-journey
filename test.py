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
        left=2
        right=4
        temp=self.head
        c=0
        while temp:
            if c+1 == left:
                first=temp
                start = temp.next
            if c == right:
                end = temp
                last=temp.next
            c+=1
            temp=temp.next
        return start,end,first,last
            
ll=LinkedList()
for i in range(1,6):
    ll.insert(i)
l,r,f,la=ll.rev()
print(l.data,r.data,f.data,la.data)
ll.display()
     