#python2

cd ~/Documents/Personal/data_structures/data_structures_implementation/

from linked_list import *

##### Defining class queues
class queue(singlylinkedlist):
### Initializing the queue
     def __init__(self):
         self.head = None
         self.tail = None
### Add key to the bottom of the queue
     def enqueue(self , arg):
         self.push_back(arg)
### Extract and remove the top key from the queue`
     def dequeue(self):
         self.front = self.top()
         self.pop_front()
         return  self.front
### Check if the list is empty?
     def empty(self):
         if self.head == None:
             return 1
         else:
             return 0
