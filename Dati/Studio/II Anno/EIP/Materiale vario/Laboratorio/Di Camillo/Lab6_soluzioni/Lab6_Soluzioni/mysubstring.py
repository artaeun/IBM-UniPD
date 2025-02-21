# mysubstring.py (modulo)

def getAllSubstrings(s) :
   subs = [""] # prima sottostringa "impropria"
   # per ogni possibile lunghezza di sottostringa...
   for i in range(1, len(s)) : 
      # per ogni possibile posizione iniziale di
      # una sottostringa di lunghezza i...
      for j in range(len(s) - i + 1) : 
         subs.append(s[j : j + i])
   if len(s) > 0 :
      subs.append(s) # ultima sottostringa "impropria",
                     # solo se s non è vuota altrimenti risulta doppia
   return subs
   
def numSubstrings(s) :
   return 1 + len(s) * (len(s) + 1) // 2
   
def areUnique(ss) :
   for i in range(len(ss)) :
      for j in range(i + 1, len(ss)) :
         if ss[i] == ss[j] :
            return False
   return True
   
def isSortedByIncreasingLength(ss) :
   for i in range(1, len(ss)) :
      if len(ss[i - 1]) > len(ss[i]) :
         return False
   return True
   
def isSortedByDecreasingLength(ss) :
   for i in range(1, len(ss)) :
      if len(ss[i - 1]) < len(ss[i]) :
         return False
   return True 
      
def isForwardSorted(ss) : # lexicographically
   for i in range(1, len(ss)) :
      if ss[i - 1] > ss[i] :
         return False
   return True
   
def isBackwardSorted(ss) : # lexicographically
   for i in range(1, len(ss)) :
      if ss[i - 1] < ss[i] :
         return False
   return True
      
def isSorted(ss) :
   return isForwardSorted(ss) 

def isSubstring(s1, s2) :
   return s1 in s2

def isSubsequence(s1, s2) :
   k = j = 0
   while j < len(s1) and k < len(s2) :
      if s2[k] == s1[j] :
         j += 1
      k += 1
   return j == len(s1)

def getAllSubsequences(s) :
   subs = []
   for i in range(2 ** len(s)) :
      new = ""
      j = 0
      num = i
      while num > 0 :
         if num % 2 == 1 :
            new += s[j]
         num //= 2
         j += 1         
      subs.append(new)
   return subs
   
def numSubsequences(s) :
   return 2 ** len(s)
