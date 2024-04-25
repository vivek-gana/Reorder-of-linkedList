class Node:
    def __init__(self,data):
        self.data=data
        self.mext=none
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def addnode(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=new_node
            self.tail=newNode
    def display(self):
        current=current.head
        if(self.head==None):
            print("list is empty")
            return;
        while(current!=None):
            print(current.data)
            currenr=current.next
    S=LinkedList():
    s.addNode(4)
    s.addNode(5)
        
