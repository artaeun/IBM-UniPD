# eratostene.py
from myinput import *
MAX = inputPositiveDecimalInteger("Un numero intero positivo: ")
primes = [True] * MAX
"""
   osservo che le prime due celle della lista sono "sprecate",
   per risparmiare potrei usare MAX-2 come dimensione e poi dire che
   il numero x è rappresentato dalla cella di indice x-2, ma per due
   sole celle non vale la pena
"""
for i in range(2, MAX) :
   # il primo multiplo di i, che devo "eliminare", è 2*i
   for j in range(2*i, MAX, i) : # uso anche il terzo parametro
      primes[j] = False
   """
      nel ciclo più esterno qui sopra, il valore finale di i potrebbe
      essere limitato a MAX/2: numeri maggiori o uguali a MAX/2 hanno
      il loro primo multiplo (il doppio) che è già maggiore di MAX-1,
      quindi non "eliminano" nessun altro numero
   """
print("Numeri primi minori di %i:" % MAX)
for i in range(2, MAX) :
   if primes[i] :
      print(i, end=' ')
print()