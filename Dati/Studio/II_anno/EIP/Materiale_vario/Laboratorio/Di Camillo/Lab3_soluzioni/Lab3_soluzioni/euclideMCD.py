# euclideMCD.py
from sys import exit
m = int(input("Primo numero (intero positivo)? "))
n = int(input("Secondo numero (intero positivo)? "))
if m <= 0 or n <= 0 :
   exit("Non sono due numeri positivi")
origM = m # servono per poi visualizzare il risultato
origN = n # perché m e n vengono modificati
# Faccio in modo che sia m >= n
if m < n :
   # scambio m con n usando una variabile temporanea
   tmp = m
   m = n
   n = tmp
# ora certamente m >= n 
# Algoritmo di Euclide
while m % n != 0 :
   tmp = n 
   n = m % n
   m = tmp
# ora n è il MCD di origM e origN
print("MCD(" + str(origM) + "," + str(origN) + ") = " + str(n))