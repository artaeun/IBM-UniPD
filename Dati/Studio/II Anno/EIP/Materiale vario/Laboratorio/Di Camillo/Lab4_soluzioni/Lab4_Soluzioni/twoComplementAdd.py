# twoComplementAdd.py
from sys import exit
s1 = input("Primo numero in complemento a due: ")
s2 = input("Secondo numero (con la stessa lunghezza): ")
if len(s1) != len(s2) :
   exit("I due numeri non hanno la stessa lunghezza")
i = 0
while i < len(s1) :
   if s1[i] != "0" and s1[i] != "1" :
      exit("Il primo numero non è binario")
   i += 1
i = 0
while i < len(s2) :
   if s2[i] != "0" and s2[i] != "1" :
      exit("Il secondo numero non è binario")
   i += 1
      
result = "" # conterrà il risultato
lastCarryBit = 0       # ultimo riporto
lastButOneCarryBit = 0 # penultimo riporto
# le due inizializzazioni precedenti rendono funzionante l'algoritmo
# anche quando i numeri hanno una sola cifra (verificare...)
carryBit = 0           # riporto dalla colonna precedente, 
                       # per la colonna più a destra (la prima) vale 0
# ora faccio l'addizione in colonna, OVVIAMENTE da destra a sinistra!
i = len(s1) - 1 # indice della cifra più a destra
while i >= 0 :
   if s1[i] == '0' : firstBit = 0
   else : firstBit = 1
   if s2[i] == '0' : secondBit = 0
   else : secondBit = 1
   addedBits = firstBit + secondBit + carryBit
   resultBit = addedBits % 2
   result = str(resultBit) + result # perché non result += str(resultBit) ?
   carryBit = addedBits // 2 # riporto sulla prossima colonna
   if i == 0 : # ho appena sommato la colonna più a sinistra,
               # quindi memorizzo l'ultimo riporto
      lastCarryBit = carryBit
   if i == 1 : # ho appena sommato la penultima colonna più a sinistra,
               # quindi memorizzo il penultimo riporto
      lastButOneCarryBit = carryBit
   i -= 1 # DECREMENTO l'indice per andare da destra a sinistra
   # l'ultimo riporto generato non contribuisce (correttamente) al risultato
   # come previsto dall'algoritmo di addizione in complemento a due

print(s1 + " + " + s2 + " = " + result)
if lastCarryBit != lastButOneCarryBit :
   print("Overflow")