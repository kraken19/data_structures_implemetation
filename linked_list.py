# python2


##### List being initialized with any variable (not necessary a node) e.g. y = singlylinkedlist(5)

#### Defining a class Node
class node():
    def __init__(self , key):
        self.key = key
        self.next = None
        self.previous = None
        self.l = 0

#### Defining class linkedlist

class singlylinkedlist():
### Initialize the object
    def __init__(self):
            self.head = None
            self.tail = None
### Add node to front of list
    def push_front(self , arg):
        self.l +=1
        Node = node(arg)
        Node.next = self.head
        self.head = Node
        if self.tail == None:
            self.tail = self.head
        #del self.next
### Extract the top value in the list
    def top(self):
        if self.head == None:
            print "Error : Empty object"
        else:
            return self.head.key
### Remove the 1st value from the list
    def pop_front(self):
        if self.head == None:
            print "Empty object"
        else:
            self.l -= 1
            self.head = self.head.next
            #self.next = pointer(self.head)
            if self.head == None:
                self.tail = None
### Add node to back of list
    def push_back(self , arg):
        self.l + = 1
        Node = node(arg)
        if self.tail == None:
            self.head = Node
            self.tail = Node
        else:
            self.tail.next = Node
            self.tail = Node
### Return the bottom value from the list
    def bottom(self):
        if self.tail == None:
            print "Error : Empty object"
        else:
            return self.tail.key
### Removes the last value from the list
    def pop_last(self):
        if self.head == None:
            print "Error : Empty object"
        else:
            self.l -=1
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                p = self.head
                while p.next.next != None:
                    p = p.next
                self.tail = p
                p.next = None
### Calculate the no of elements in the list
    def length(self):
        if self.head == None:
            return 0
        else:
            if self.head == self.tail:
                return 1
            else:
                p = self.head
                i = 1
                while p.next.next != None:
                    p = p.next
                    i+= 1
                return i+1
### Find a key in the list
    def find(self, arg):
        if self.head == None:
            print "Error : Empty object"
            return 0
        else:
            find = self.head
            i = 0
            while find:
                if find.key == arg:
                    i+=1
                    break
                else:
                    find = find.next
            if i >0:
                return 1
            else:
                return 0
### Erase a key from the list
    def erase(self , arg):
        if self.head == None:
            print "Error : Empty object"
            return 0
        else:
            if self.head.key == arg:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            else:
                erase = self.head
                i = 0
                while erase.next:
                    if erase.next.key == arg:
                        i+=1
                        erase.next = erase.next.next
                        if erase.next == None:
                            self.tail = erase
                        break
                    else:
                        erase = erase.next
                if i == 0:
                    print "Error : Key not present in the object"
### Add a node after a certain position
    def add_after(self , position , arg):
        if position <= 0:
            print "Error: position argument needs to be positive"
        else:
            self.l + =1
            l1 = self.length()
            if position >= l1 or l1==1:
                self.push_back(arg)
                if  position > l1:
                    print "Warning : Position is greater than the size of the object. Appended data to end of object"
            else:
                i = 1
                p = self.head
                while i < position:
                    i+=1
                    p = p.next
                Node = node(arg)
                Node.next = p.next
                p.next = Node
### Add a node before a certain position
    def add_before(self , position , arg):
        self.add_after(self , position-1 , arg)





#        if position <= 0:
#            print "Error: position argument needs to be positive"
#        else:
#            l = self.length()
#            if position > l:
#                self.push_back(arg)
#                print "Warning : Position is greater than the size of the list. Appended data to end of list"
#            elif  l==1:
#                self.push_front(arg)
#            else:
#                i = 1
#                p = self.head
#                while i < position-1:
#                    i+=1
#                    p = p.next
#                Node = node(arg)
#                Node.next = p.next
#                p.next = Node
#
#y = singlylinkedlist()
#y.push_front(10)
#y.push_front(15)
#y.push_front(20)
#y.erase(10)
#y.top()
