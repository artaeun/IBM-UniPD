# testSubstring.py
from mysubstring import *

def reverse(s) :
   for i in range(len(s) // 2) :
      temp = s[i]
      s[i] = s[-i-1]
      s[-i-1] = temp

for s in ["", "a", "ab", "abc", "abcdefghilm"] :
   print('"' + s + '"')
   ss = getAllSubstrings(s)
   print("Sottostringhe, valore previsto:", numSubstrings(s))
   print("Sottostringhe, valore effettivo:", len(ss)) 
   if len(ss) != numSubstrings(s) :
      print("      ERRORE !!")
   if areUnique(ss) :
      print("Le sottostringhe sono tutte diverse")
   else :
      print("ERRORE !! Le sottostringhe NON sono tutte diverse")
   ss.sort()
   if not isForwardSorted(ss) :
      print("ERRORE !! Il metodo isForwardSorted non funziona")
   reverse(ss)
   if not isBackwardSorted(ss) :
      print("ERRORE !! Il metodo isBackwardSorted non funziona")
   ss = getAllSubsequences(s)
   print("Sottosequenze, valore previsto:", numSubsequences(s))
   print("Sottosequenze, valore effettivo:", len(ss)) 
   if len(ss) != numSubsequences(s) :
      print("      ERRORE !!")
   if areUnique(ss) :
      print("Le sottosequenze sono tutte diverse")
   else :
      print("ERRORE !! Le sottosequenze NON sono tutte diverse")