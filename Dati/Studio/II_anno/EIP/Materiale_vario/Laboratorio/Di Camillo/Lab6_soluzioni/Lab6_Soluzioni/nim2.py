# nim2.py
from random import randint
def main() :
   while True : # terminerà (ovviamente) con un break
      # inizio di una (nuova) partita
      numBalls = randint(10, 100)
      computerPlayerIsExpert = randomBoolean()
      nextPlayerIsHuman = randomBoolean()
      while numBalls > 1 :
         if nextPlayerIsHuman : # è il turno del giocatore umano
            numBalls -= askUserBalls(numBalls)
         else : # è il turno del computer
            taken = takeComputerBalls(computerPlayerIsExpert, numBalls)
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
      if not playAgain() :
         break
         
def askUserBalls(numBalls) :
   while True :
      print("Biglie presenti nel mucchio: ", numBalls)
      taken = int(input("Quante ne vuoi prendere? "))
      if taken < 1 or taken > (numBalls // 2) : # attenzione che sia corretto anche se dispari...
         print("Azione errata")
      else :
         return taken # il giocatore umano ha fatto una scelta valida
                      # return interrompe la funzione... quindi anche il ciclo!

def takeComputerBalls(computerPlayerIsExpert, numBalls) :
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
   return taken
         
def playAgain() :        
   while True :
      response = input("Vuoi giocare ancora? (S/N) ")
      if response.upper() == "N" :
         return False
      if response.upper() == "S" :
         return True 

from random import random
def randomBoolean() :
   if random() < 0.5 :
      return True
   return False # perché qui non serve else ?
         
main()