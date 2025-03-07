# printPerfectMagicSquare.py
from sys import exit
from myinput import *

while True :
   n = inputPositiveDecimalInteger("")
   if n % 2 == 1 : # numero dispari
      break
      
matrix = []
# riempio la matrice di zeri, che durante l'esecuzione dell'algoritmo
# di generazione del quadrato magico significheranno "posizione non
# ancora scritta", perché 0 non è un valore valido nel quadrato
for i in range(n) :
   matrix.append([0]*n) # ogni riga ha n zeri

# eseguo l'algoritmo suggerito
row = n - 1
column = n // 2
for k in range(1, 1 + n * n) :
   matrix[row][column] = k
   # devo memorizzare i valori attuali di row e column per poter
   # "ripristinare i loro valori precedenti", come previsto dall'algoritmo
   oldrow = row
   oldcolumn = column
   row += 1
   column += 1
   if row == n : row = 0
   if column == n : column = 0
   if matrix[row][column] != 0 :
      row = oldrow
      column = oldcolumn
      row -= 1

# visualizzo il quadrato generato, con le spaziature opportune
width = len(str(n*n))
for i in range(n) :
   for j in range(n) :
      print(("%" + str(width) + "i") % matrix[i][j], end=" ")
   print()