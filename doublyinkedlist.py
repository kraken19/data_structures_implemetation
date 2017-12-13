object# python2

##### Empty object being initialized with any variable (not necessary a node) e.g. y = singlylinkedlist(5)
########### Double linkedlist

#### Defining a class Node
class node():
    def __init__(self , key):
        self.key = key
        self.next = None
        self.previous = None

#### Defining class linkedlist
class doublylinkedlist():
### Initializing object
    def __init__(self):
            self.head = None
            self.tail = None
### Add node to front of the list
    def push_front(self , arg):
        Node = node(arg)
        Node.next = self.head
        self.head.previous = Node
        self.head = Node
        if self.tail == None:
            self.tail = self.head
        #del self.next
### Extract key from top node
    def top(self):
        if self.head == None:
            print "Error : Empty object"
        else:
            return self.head.key
### Remove the top node from the list
    def pop_front(self):
        if self.head == None:
            print "Empty object"
        else:
            self.head = self.head.next
            #self.next = pointer(self.head)
            if self.head == None:
                self.tail = None
            else:
                self.head.previous = None
### Add node to end of list
    def push_back(self , arg):
        Node = node(arg)
        if self.tail == None:
            self.head = Node
            self.tail = Node
        else:
            Node.previous = self.tail
            self.tail.next = Node
            self.tail = Node
### Extract key from bottom node
    def bottom(self):
        if self.tail == None:
            print "Error : Empty object"
        else:
            return self.tail.key
### Remove the bottom node from the list
    def pop_last(self):
        if self.head == None:
            print "Error : Empty object"
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.previous
                self.tail.next = None
### Calculate the length of the list
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
### Find key in the list
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
### Erase key from the list
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
                    self.head.previous = None
            else:
                erase = self.head
                i = 0
                while erase:
                    if erase.key == arg:
                        i+=1
                        if erase.next == None:
                            self.tail = erase.previous
                            self.tail.next = None
                            erase.previous = None
                            erase.key = None
                        else:
                            erase.previous.next = erase.next
                            erase.next.previous = erase.previous
                            erase.previous = None
                            erase.next = None
                            erase.key = None
                        break
                    else:
                        erase = erase.next
                if i == 0:
                    print "Error : Key not present in the object"
### Add node after a certain position
    def add_after(self , position , arg):
        if position <= 0:
            print "Error: position argument needs to be positive"
        else:
            l = self.length()
            if position >= l or l==1:
                self.push_back(arg)
                if  position > l:
                    print "Warning : Position is greater than the size of the object. Appended data to end of object"
            else:
                i = 1
                p = self.head
                while i < position:
                    i+=1
                    p = p.next
                Node = node(arg)
                Node.next = p.next
                Node.previous = p
                p.next.previous = Node
                p.next = Node
### Add node before a certain position
    def add_before(self , position , arg):
        self.add_after(self , position - 1 , arg)
