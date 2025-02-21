# isSubsequence.py
s1 = input("Prima stringa: ")
s2 = input("Seconda stringa: ")
foundSubsequence = False
k = j = 0
while j < len(s2) and k < len(s1) :
   if s1[k] == s2[j] :
      j += 1 # trovato in s1[k] il j-esimo carattere di s2
   k += 1 # procedo in s1
if j == len(s2) :
   # tutti i caratteri di s2 sono stati trovati in s1, nell'ordine corretto
   foundSubsequence = True
print("La seconda stringa", end="")
if not foundSubsequence :
   print(" non", end="")
print(" è una sottosequenza della prima")
