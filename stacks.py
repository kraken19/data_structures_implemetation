#python2

from linked_list import *

#### Defining the class stacks
class stacks(singlylinkedlist):
### Initializing the stack
     def __init__(self):
         self.head = None
         self.tail = None
### Add key to top of stack
     def push(self , arg):
         self.push_front(arg)
### Extract value from top of stack
     def get(self):
         return self.top()
### Remove the top value from the stack
     def pop(self):
         return self.pop_front()
### is the stack empty?
     def empty(self):
         if self.head == None:
             return 1
         else:
             return 0
