# stackandqueue.py (modulo)

class EmptyStackError(BaseException):
   pass
   
class EmptyQueueError(BaseException):
   pass
   
class Stack :

   def __init__(self) :
      self._list = list() # lista vuota, cioè pila vuota

   def __len__(self) :
      return len(self._list)

   def push(self, element) :
      self._list.append(element)

   def pop(self) :
      if self.__len__() == 0 : raise EmptyStackError
      return self._list.pop()

   def top(self) :
      if self.__len__() == 0 : raise EmptyStackError
      return self._list[-1]

class Queue :

   def __init__(self) :
      self._list = list() # lista vuota, cioè coda vuota

   def __len__(self) :
      return len(self._list)

   def enqueue(self, element) :
      self._list.append(element)

   def dequeue(self) :
      if self.__len__() == 0 : raise EmptyQueueError
      return self._list.pop(0)

   def front(self) :
      if self.__len__() == 0 : raise EmptyQueueError
      return self._list[0]
