# stackWithSpecialPush.py (modulo)

class EmptyStackError(BaseException):
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

class SpecialStack(Stack) :

   # il costruttore non serve
      
   def contains(self, e) :
      return e in self._list
      # senza accedere direttamente alla lista, avrei dovuto svuotare
      # "me stesso", conservando i valori in una lista temporanea
      # (o, meglio, una pila temporanea), per poi reimpilarli
      
   def push(self, element) :
      if not self.contains(element) :
         super().push(element)
         
if __name__ == "__main__" :
   def error() : print("ERRORE")
   s = SpecialStack()
   s.push(1)
   s.push(2)
   s.push(0)
   s.push(2)
   if len(s) != 3 : error()
   s.pop()
   s.push(2)
   s.push(0)
   s.push(0)
   if len(s) != 3 : error()
   