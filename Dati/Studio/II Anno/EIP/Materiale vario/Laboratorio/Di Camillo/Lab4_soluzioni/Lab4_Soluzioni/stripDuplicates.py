# stripDuplicates.py
s = input("Stringa: ")

# l'esercizio si può risolvere in tanti modi diversi...
# riporto due esempi

i = 0
while i < len(s) - 1 : # attenzione al -1
   if s[i] == s[i + 1] : # uso s[i+1], è importante il -1 qui sopra...
      s = s[:i] + s[i+1:] # COSA FA ?
   else :
      i += 1 # perché nel corpo dell'if non incremento i ?
print(s)
"""
# soluzione alternativa: più veloce, perché non costruisce 
# sottostringhe né stringhe
if len(s) > 0 : # stringa vuota? non faccio niente...
   # visualizzo il primo carattere
   print(s[0], end="")
   # i caratteri successivi al primo vengono visualizzati 
   # se e solo se sono diversi dal carattere precedente
   i = 1 # attenzione: parto da 1
   while i < len(s) :
      if s[i] != s[i - 1] : # uso s[i-1], è importante partire da i=1
         print(s[i], end="")
      i += 1
   print() # ho finito, vado a capo
"""