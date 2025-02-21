# isPerfectMagicSquare.py
from sys import exit

matrix = []

while True :
   s = input()
   if s == "" :
      break
   row = [] # riga che costruirò, leggendo i numeri in s
   i = 0
   # ignoro eventuali spazi iniziali
   while i < len(s) and s[i] == ' ' : i += 1
   # cerco i numeri nella stringa s, 
   while i < len(s) :
      j = i # forse inizia un numero 
      while i < len(s) and s[i].isdigit() : i += 1 # "consuma" cifre
      if i == j : # non c'erano cifre, non era un numero
          exit("Errore nella riga %i" % (1 + len(matrix))) 
      # aggiungo il numero alla fine della riga che sto costruendo
      row.append(int(s[j:i]))
      # "consumo" gli spazi seguenti, fino al prossimo numero oppure alla fine
      # della stringa s
      while i < len(s) and s[i] == ' ' : i += 1 
   # ho costruito una riga della matrice, la aggiungo alla matrice
   matrix.append(row)
   # se la riga appena aggiunta non è la prima riga, deve essere
   # lunga come le precedenti
   if len(matrix) != 0 : 
      if len(row) != len(matrix[0]) :
         if len(row) < len(matrix[0]) :
            exit("Riga %i troppo corta" % len(matrix))
         else :
            exit("Riga %i troppo lunga" % len(matrix))
   # se la matrice è quadrata, ho finito di leggere dati
   if len(matrix) == len(matrix[0]) :
      break
      
if len(matrix) == 0 : exit("Scrivi almeno un numero!") # matrice rimasta vuota!
size = len(matrix) # dimensione del quadrato (numero di righe e di colonne)
num = size * size  # numero massimo che deve essere presente nel quadrato
      
# verifico che siano presenti tutti i numeri da 1 a num, senza duplicati
for i in range(1, num+1) :
   # cerco il numero i
   found = False
   for row in matrix :
      for val in row :
         if val == i :
            found = True
            break
      if found : break
   if not found : exit("Manca il numero %i" % i)
"""
   il ciclo precedente verifica soltanto che i numeri da 1 a N ci siano tutti,
   senza controllare la presenza di eventuali duplicati, perché
   è facile dimostrare che, se in un elenco di N numeri ci sono
   tutti i numeri da 1 a N, non ci possono essere duplicati
"""

# visualizzo la matrice
width = len(str(num))
for i in range(size) :
   for j in range(size) :
      print(("%" + str(width) + "i") % matrix[i][j], end=" ")
   print()
# verifico le regole di magicità...
magicnumber = sum(matrix[0]) # somma dei valori della prima riga
# ... controllo che le altre righe siano uguali
for i in range(1, size) : # inutile controllare la prima riga...
   if sum(matrix[i]) != magicnumber :
      exit("La riga %i è sbagliata" % (i+1))
# ... controllo le colonne (sommare una colonna è un po' più complicato)
for i in range(size) :
   temp = 0
   for j in range(size) :
      temp += matrix[j][i]
   if temp != magicnumber :
      exit("La colonna %i è sbagliata" % (i+1))
# ... controllo le due diagonali principali
temp = 0
for i in range(size) :
   temp += matrix[i][i]
if temp != magicnumber :
   exit("La diagonale dall'angolo superiore sinistro è sbagliata")
temp = 0
for i in range(size) :
   temp += matrix[i][size - i - 1] # ATTENZIONE al secondo indice...
if temp != magicnumber :
   exit("La diagonale dall'angolo superiore destro è sbagliata")

# se sono arrivato qui, vuol dire che va tutto bene!
print("OK")