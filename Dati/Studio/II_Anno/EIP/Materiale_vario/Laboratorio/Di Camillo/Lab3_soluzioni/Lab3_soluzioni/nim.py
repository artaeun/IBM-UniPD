# nim.py
"""
   Inutile dire che un programma così lungo e articolato si può risolvere
   in molti modi diversi... questa è solo una delle possibili soluzioni
   (come sempre, ma in questo caso in modo particolare) 
"""
from random import randint, random
while True : # terminerà (ovviamente) con un break
   # inizio di una (nuova) partita
   numBalls = randint(10, 100)
   # le prossime 4 righe di codice attribuiscono un valore casuale
   # a una variabile booleana... i due valori possibili (True e False)
   # sono equiprobabili, perché uso come soglia il valore intermedio
   # dell'intervallo dei numeri generati (che va da 0 a 1);
   # usando come soglia, ad esempio, 0.3, otterrei il valore False
   # nel 30% dei casi (e, ovviamente, il valore True nel 70%), cioè
   # i due valori non sarebbero equiprobabili (ma a volte può essere
   # utile anche tale situazione)
   if random() < 0.5 :
      computerPlayerIsExpert = False
   else :
      computerPlayerIsExpert = True
   # le prossime 4 righe di codice attribuiscono un valore casuale
   # a una variabile booleana...
   if random() < 0.5 :
      nextPlayerIsHuman = False
   else :
      nextPlayerIsHuman = True
   while numBalls > 1 :
      if nextPlayerIsHuman : # è il turno del giocatore umano
         repeat = True
         while repeat :
            print("Biglie presenti nel mucchio: ", numBalls)
            taken = int(input("Quante ne vuoi prendere? "))
            if taken < 1 or taken > (numBalls // 2) : # attenzione che sia corretto anche se dispari...
               print("Azione errata") # repeat rimane True
            else :
               numBalls -= taken
               repeat = False # il giocatore umano ha fatto una scelta valida
      else : # è il turno del computer
         if not computerPlayerIsExpert : # computer "stupido"
            # deve prendere almeno una biglia e un numero di biglie
            # che non superi la metà di quelle presenti...
            # verificare che la scelta sia valida sia in caso di numero
            # di biglie pari sia in caso di numero di biglie dispari
            taken = randint(1, numBalls // 2)
         else : # computer "intelligente"
            if (numBalls == 3 or numBalls == 7 or numBalls == 15 
                or numBalls == 31 or numBalls == 63) :
               # temporaneamente stupido... deve scegliere a caso
               taken = randint(1, numBalls // 2)
            elif numBalls > 63 : # attenzione all'ordine in cui faccio i confronti...
               taken = numBalls - 63
            elif numBalls > 31 :
               taken = numBalls - 31
            elif numBalls > 15 :
               taken = numBalls - 15
            elif numBalls > 7 :
               taken = numBalls - 7
            elif numBalls > 3 :
               taken = numBalls - 3
            else : # ci sono certamente 2 biglie
               taken = 1
         print("Biglie presenti nel mucchio: ", numBalls)
         print("Il computer ne ha prese: ", taken)
         numBalls -= taken
      # cosa fa l'enunciato seguente? si usa spesso per cambiare il
      # valore di una variabile booleana
      nextPlayerIsHuman = not nextPlayerIsHuman 
   # a questo punto numBalls vale certamente 1
   # quindi chi deve fare la prossima mossa ha perso
   if nextPlayerIsHuman :
      print("Hai perso")
   else :
      print("Hai vinto!!")
   if computerPlayerIsExpert :
      print('Il computer giocava in modo "intelligente"')
   else :
      print('Il computer giocava in modo "stupido"') 
   while True :
      response = input("Vuoi giocare ancora? (S/N) ")
      if response.upper() == "N" :
         playAgain = False
         break
      elif response.upper() == "S" :
         playAgain = True 
         break
   if not playAgain :
      break