# factoring.py

from myinput import *
while True :
   num = inputPositiveDecimalInteger("Numero intero da scomporre: ")
   if num > 1 :
      break
"""
   cercando i divisori in ordine crescente, un eventuale
   divisore è certamente primo: se così non fosse, si
   sarebbe trovato prima di esso un suo divisore che
   sarebbe stato anche divisore di num
   esempio: se num è divisibile per 4 (che non è primo)
   l'algoritmo trova prima il divisore 2 (che, essendo
   divisore di 4, è certamente anche divisore di num),
   lo visualizza e, all'iterazione successiva, verrà nuovamente
   trovato il divisore 2, come deve essere, dato che num
   era divisibile per 4 = 2 * 2
"""
i = 2
while i <= num : # il segno uguale serve quando il numero è primo:
                 # in tal caso il suo unico divisore è il numero stesso
   if num % i == 0 : # num è divisibile per i
      num //= i # così num contiene il numero che rimane da scomporre
      print(i, end=" ") # spazio separatore...
      # NON incremento i, perché ci possono essere più fattori uguali!
   else :
      i += 1
"""
   attenzione a questo ciclo... non è un vero e proprio ciclo a contatore,
   perché ci sono iterazioni del ciclo che NON fanno aumentare il contatore!
"""