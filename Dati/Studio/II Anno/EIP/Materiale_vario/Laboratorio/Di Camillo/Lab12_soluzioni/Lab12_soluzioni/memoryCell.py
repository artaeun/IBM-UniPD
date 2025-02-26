# memoryCell.py (modulo)

class MemoryCell :
   def __init__(self, v) :
      self._val = v
      
   def getVal(self) :
      return self._val
      
   def setVal(self, newVal) :
      self._val = newVal
      
   def clear(self) :
      self.setVal(0)
      
class IllegalStateError(BaseException) :
   pass
   
class BackupMemoryCell(MemoryCell) :

   def __init__(self, v) :
      super().__init__(v)
      self._restoreIsAllowed = False
	  self._backupValue = None
      
   def setVal(self, newVal) :
      self._backupValue = self.getVal()
      super().setVal(newVal)
      self._restoreIsAllowed = True
      
   def restore(self) :
      if not self._restoreIsAllowed :
         raise IllegalStateError
      super().setVal(self._backupValue)
      self._restoreIsAllowed = False
      
if __name__ == "__main__" :
   def error() : print("ERRORE")
   m = BackupMemoryCell(2)
   if m.getVal() != 2 : error()
   m.setVal(3)
   if m.getVal() != 3 : error()
   m.restore()
   if m.getVal() != 2 : error()
   try :
      m.restore()
      error() # non deve arrivare qui, deve sollevare eccezione...
   except IllegalStateError :
      pass # OK
   m.setVal(4)
   if m.getVal() != 4 : error()
   m.restore()
   if m.getVal() != 2 : error()
