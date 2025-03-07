# isSubstring.py
s1 = input("Prima stringa: ")
s2 = input("Seconda stringa: ")
foundSubstring = False
# l'inizializzazione precedente significa
# "non ho ancora trovato la sottostringa", quindi è corretta
i = 0
while i < len(s1) - len(s2) + 1 and not foundSubstring :
   """
      cerchiamo s2 in s1 a partire dal carattere i-esimo di s1

      appena troviamo una corrispondenza, questo ciclo termina
      (osservate la condizione di terminazione, con l'operatore and)

      osservate il valore massimo assunto da i: non ha senso cercare
      in s1 a partire da una posizione in cui il numero di caratteri
      successivi è minore del numero di caratteri presenti in s2 !!
   """
   if s1[i : i + len(s2)] == s2 :
      foundSubstring = True
   i += 1
   
print("La seconda stringa", end="")
if not foundSubstring :
   print(" non", end="")
print(" è una sottostringa della prima")
"""
   Cosa succede se s2 è la stringa vuota?
   Il programma dovrebbe segnalare che s2 è una sottostringa,
   indipendentemente dal contenuto di s1...
   Lo fa? Perché?
   Cosa succede se s1 è la stringa vuota?
   Il programma dovrebbe segnalare che s2 è una sottostringa
   soltanto se anche s2 è vuota...
   Lo fa? Perché?
"""