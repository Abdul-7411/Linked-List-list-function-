## Creating A Linked List

class Node: # This class is creating a node
    def __init__(self,value): #Value is the object or data_type taking input.
        self.data = value    # storing in self.data variable
        self.next = None     # this is the address of the Linked List

class LinkedList: # This class is creating a linked list
    def __init__(self):
        #Empty Linked List 
        self.head = None
        self.node = 0 #no of nodes in the linked list

    def __len__(self): # This shows the length of the linked list by (__len__) constructor
        return self.node

    def insert_head(self,value):
        # new node
        new_node = Node(value)
        # creating connection
        new_node.next = self.head
        # reassign head
        self.head = new_node
        # increament node
        self.node = self.node +1
    
    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) +'->'
            curr = curr.next
        return result[:-2]
    
    def append(self,value):
        # new node
        new_node = Node(value)
        if self.head == None:# checking list is empty or not?
            self.head = new_node
            self.node = self.node + 1
            return 
        
        # create connection
        curr = self.head
        while curr.next != None:
            curr = curr.next
            
        # adding at last node
        curr.next = new_node
        #increment 
        self.node = self.node + 1
    
    def insert_after(self,after,value):
        curr = self.head
        new_node = Node(value)
        while curr != None:
            if curr.data == after: 
                break
            curr = curr.next
        
        if curr != None:# If curr value is not None
            #Logic
            new_node.next = curr.next
            curr.next = new_node
        else:# If curr value is None
            return "Item Not Found"
    
    def clear(self):
        self.head = None
        self.node = 0    
    
    def delete_head(self):
        if self.head == None:
            return 'Empty Linked List'
        self.head = self.head.next
    
    def pop(self):
        if self.head == None:
            return 'Empty Linked List'
        curr = self.head  
       
        if curr.next == None:
            return self.delete_head()

        while curr.next.next != None:
            curr = curr.next
            
        # remaining 2nd last node
        curr.next = None
        # decrement 
        self.node = self.node - 1  
    
    def remove(self,value):
        if self.head == None:
            return "Empty LL"
        elif self.head.data == value:
            self.delete_head()
            
        curr =self.head
        
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        
        # if item not found 
        if curr.next == None:
            return 'Item not found in LL'
        else:
            curr.next = curr.next.next
    def find(self,item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos+=1
        return 'Item Not Found'
    
    def __getitem__(self,index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos+=1
        return 'IndexError'
    
l = LinkedList()
print(len(l))
l.insert_head(1)
l.append(5)
l.insert_after(1,4)
l.delete_head()
l.find(4)
l.pop()
l.remove(4)
print(l)
l.clear()
print(l)
# print(l)