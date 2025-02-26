# twoNumbers.py
n1 = float(input("Primo numero? "))
n2 = float(input("Secondo numero? "))
print("Somma:", n1 + n2)
print("Prodotto:", n1 * n2)
print("Valore medio:", (n1 + n2) / 2) # attenzione alle necessarie parentesi...
# definisco il messaggio in una variabile per non doverlo scrivere due volte,
# cosa che sarebbe fonte di possibili errori di distrazione
massimo = "Valore massimo:"
if n1 > n2 : # sarebbe corretto scrivere >= ? cambierebbe qualcosa?
   print(massimo, n1)
else :
   print(massimo, n2)
minimo = "Valore minimo:"
if n1 < n2 : 
   print(minimo, n1)
else :
   print(minimo, n2)
differenza = "Differenza (in valore assoluto):"
if n1 - n2 < 0 : 
   print(differenza, n2 - n1)
else :
   print(differenza, n1 - n2)