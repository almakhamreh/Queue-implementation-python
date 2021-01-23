# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 12:50:32 2021

@author:  Ahmad Almakhamreh
"""

"""
   all methods return & print the appropiate values
   print statements are commented. you can always uncomment them to track the operations
"""

class Queue:
   def __init__(self):
      self.__myQueue = []
      """
      the leading underscores are simply to indicate that the attribute is inteded to be private and should not be accessed outside the class
      """


   def enqueue(self,item):
      """This method accepts an item as a parameter and inserts it into 0th index (the back) of the List & prints the added item.
      inserting into the 0th element happens in linear time, since we have to shift all the items in the list. So the runtime for this method is O(n)
      """
      self.__myQueue.insert(0, item)
      # print(f"enqueue: ---> {item}")


   def dequeue(self):
      """This method removes, returns, and prints the last item in the list, which is represented by the Front of the Queue.
      removing from the end of a list (Front)  happens in constant time, so the runtime for this method is O(1)
      """
      if self.__myQueue:
         # print(f"dequeue: ---> {self.__myQueue[-1]}" )
         return self.__myQueue.pop()
      else:
         print("cannot dequeue, Queue is empty")


   def top(self):
      """This method prints and returns the last item in the list (front-most item) without removing it
      this method runs in constant time O(1), because indexing the last item in the list is done in constant time. (Random access)
      """
      if self.__myQueue:
         print(f"top: ---> {self.__myQueue[-1]} ")
         return self.__myQueue[-1]
      else:
         print("cannot peek, stack is empty")


   def size(self):
      """This method prints & retuns the length of the list that is representing the Queue.
      this method runs in constant time O(1), because finding the length of a list also happens in constant time.
      """
      print(f"size: {len(self.__myQueue)}")
      return len(self.__myQueue)


   def isEmpty(self):
      """This method retuns a boolean value describing weather or not the Queue is empty.
      testing for equality happens in constant time.
      """
      print(f"isEmpty: ---> {self.__myQueue == []}")
      return not(self.__myQueue)
      # can also use
      # return self.__myQueue == []


   def showItems(self):
      """this method prints the items in the list"""
      print(f"BACK ---> {self.__myQueue} <---- FRONT")


def main():

   """
   Test cases
   """
   Q  = Queue()

   Q.enqueue(5)
   Q.enqueue("ahmed")
   Q.enqueue(7.0)

   Q.showItems()

   Q.enqueue('A')

   Q.showItems()
   Q.top()

   Q.dequeue()
   Q.dequeue()
   Q.dequeue()

   Q.dequeue()
   Q.dequeue()
   Q.isEmpty()

if __name__ == "__main__" : main()
