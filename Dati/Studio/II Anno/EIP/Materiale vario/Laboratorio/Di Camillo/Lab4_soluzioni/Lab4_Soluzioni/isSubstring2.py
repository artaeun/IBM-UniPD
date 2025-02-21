# isSubstring2.py
s1 = input("Prima stringa: ")
s2 = input("Seconda stringa: ")
foundSubstring = False

i = 0
while i < len(s1) - len(s2) + 1 and not foundSubstring :
   """
      nell'esercizio precedente, potendo estrarre sottostringhe
      di qualsiasi lunghezza, agivamo così:
      
         if s1[i : i + len(s2)] == s2 :
            foundSubstring = True
            
      cioè confrontavamo la stringa s2 con una specifica sottostringa
      di s1 avente lunghezza uguale a len(s2)
      
      in pratica dobbiamo realizzare lo stesso algoritmo di confronto
      tra stringhe/sottostringhe, usando i singoli caratteri
      
      ci serve un ciclo annidato che scandisce i caratteri di s2
      confrontandoli con i corrispondenti caratteri della porzione
      di s1 che inizia all'indice i

      osservare con attenzione gli indici usati nei due utilizzi 
      dell'operatore di estrazione di sottostringa di lunghezza unitaria:
      nel primo utilizzo cerchiamo il carattere j-esimo della porzione di
      s1 che inizia all'indice i   
   """
   different = False
   j = 0
   while j < len(s2) and not different :
      if s1[i + j] != s2[j] :
         different = True # questo fa anche terminare il ciclo
      j += 1
   if not different :
      # i caratteri sono tutti uguali fino alla fine di s2
      # quindi ho trovato la sottostringa
      foundSubstring = True
      """
         altrimenti è stato trovato almeno un carattere diverso,
         quindi a partire dalla posizione i in s1 NON c'è una sottostringa
         uguale a s2;
         non devo fare niente, perché foundSubstring è rimasta False e
         cercherò la sottostringa a partire dalla posizione successiva in s1
      """
   i += 1
   
print("La seconda stringa", end="")
if not foundSubstring :
   print(" non", end="")
print(" è una sottostringa della prima")