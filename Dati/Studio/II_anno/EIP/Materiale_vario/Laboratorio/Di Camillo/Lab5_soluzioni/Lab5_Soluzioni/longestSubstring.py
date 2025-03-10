# longestSubstring.py
s1 = input("Prima stringa: ")
s2 = input("Seconda stringa: ")

longest = ""
for i in range(len(s1)) :
   # i è l'indice di inizio della sottostringa in s1
   for j in range(len(s2)) :
      # j è l'indice di inizio della sottostringa in s2
      k = 0 # k è la lunghezza della sottostringa comune che sto cercando
      while i + k < len(s1) and j + k < len(s2) :
         if s1[i + k] != s2[j + k] :
            break # la sottostringa comune è finita e ha lunghezza k (anche zero...)
         k += 1
      if k > len(longest) :
         longest = s1[i : i + k] # oppure s2[j : j + k], è indifferente
         """
            se esistono più sottostringhe comuni aventi la stessa
            lunghezza, nel qual caso le specifiche del programma sono
            incomplete, questo programma sceglie quella che si trova
            più a sinistra in s1
            
            scrivendo >= invece di > in questo if si sceglierebbe,
            al contrario, quella più a destra in s1
         """

print("La più lunga sottostringa comune a ", end="")
print('"' + s1 + '" e "' + s2 + '" è "' + longest + '"')
"""
   ecco ora una soluzione un po' più veloce... come mai? funziona?

   i = 0
   while i < len(s1) - len(longest) : # qui è cambiato l'intervallo
      j = 0
      while j < len(s2) - len(longest) : # qui è cambiato l'intervallo
         # poi è tutto come prima...
         k = 0
         while i + k < len(s1) and j + k < len(s2) :
            if s1[i + k] != s2[j + k] :
               break
            k += 1
         if k > len(longest) :
            longest = s1[i : i + k]
         j += 1
      i += 1
            
   perché non ho scritto i due cicli più esterni con un for ?
   
   for i in range(len(s1) - len(longest)) :
      for j in range(len(s2) - len(longest)) :
         k = 0
         ...
         
   cosa succede in questo caso? funziona? risparmia tempo?
            
"""