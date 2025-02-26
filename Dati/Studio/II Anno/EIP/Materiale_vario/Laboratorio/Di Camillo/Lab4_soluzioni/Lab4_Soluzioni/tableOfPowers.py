# tableOfPowers.py
from sys import exit

print("Tavola Pitagorica fino a x elevato alla y")
maxX = int(input("Valore massimo della base? "))
maxY = int(input("Valore massimo dell'esponente? "))
if maxX < 1 or maxY < 1 :
   exit("Errore")

x = 1
while x <= maxX :
   y = 1
   while y <= maxY :
      # calcolo la lunghezza del massimo numero in questa colonna
      maxValue = maxX ** y
      columnLength = len(str(maxValue))
      if y != 1 : # nella sola prima colonna NON aggiungo uno spazio
         columnLength += 1
      # creo la stringa di formato per l'operatore % nel print
      formatString = "%" + str(columnLength) + "s"
      # visualizzo il numero preceduto dagli spazi che servono
      print(formatString % x ** y, end="")
      y += 1
   print() # ho scritto una riga completa, vado a capo
   x += 1
   
# soluzione alternativa senza usare l'operatore di formato per le stringhe,
# stampando gli spazi che servono con un ciclo
"""
x = 1
while x <= maxX :
   y = 1
   while y <= maxY :
      maxValue = maxX ** y
      columnLength = len(str(maxValue))
      if y != 1 : # non è la prima colonna
         columnLength += 1
      value = x ** y
      spaces = columnLength - len(str(value))
      i = 0
      while i < spaces :
         print(" ", end="")
         i += 1
      print(value, end="")
      y += 1
   print()
   x += 1
"""