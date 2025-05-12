# nim3.py
from random import randint, random

def main() :
   while True : 
      # inizio di una (nuova) partita
      game = NimGame()
      game.play()         
      while True :
         response = input("Vuoi giocare ancora? (S/N) ")
         if response.upper() == "N" or response.upper() == "S" :
            break
      if response.upper() == "N" :
         break
         
class NimPile :
   def __init__(self, numBalls) :
      if numBalls < 1 :
         raise ValueError("Error in NimPile constructor: " + str(numBalls))
      self._numBalls = numBalls
      
   def getTotal(self) :
      return self._numBalls
   
   def take(self, takenBalls) :
      if takenBalls < 1 or takenBalls > self._numBalls // 2 :
         raise ValueError("Error in NimPile take method: " + str(takenBalls))
      self._numBalls -= takenBalls
      
class NimHumanPlayer :
   # non ha bisogno di variabili di esemplare,
   # quindi non serve un costruttore;
   # i due tipi di giocatori (umano e computer)
   # si distinguono per il modo in cui giocano
   # cioè per l'algoritmo del loro metodo move()
   def move(self, pile) : # non usa il parametro self, perché non ha variabili di esemplare
      while True :
         numBalls = pile.getTotal()
         print("Biglie presenti nel mucchio:", numBalls)
         taken = input("Quante ne vuoi prendere? ")
         try :
            taken = int(taken)
            if taken >= 1 and taken <= (numBalls // 2) :
               pile.take(taken) # eseguo la mossa         
               return
            print("Mossa errata: riprova!")
         except ValueError :
            print("Mossa errata: riprova!")
   
class NimComputerPlayer :
   # ha un'unica variabile di esemplare, che discrimina tra modalità
   # "esperta" o "stupida"
   def __init__(self, isExpert) :
      self._isExpert = isExpert
      
   def isExpert(self) :
      return self._isExpert
       
   def move(self, pile) :
      n = pile.getTotal()
      if self._isExpert :
         if n == 3 or n == 7 or n == 15 or n == 31 or n == 63 :
            # temporaneamente stupido...
            taken = randint(1, n // 2)
         elif n > 63 : 
            taken = n - 63
         elif n > 31 :
            taken = n - 31
         elif n > 15 :
            taken = n - 15
         elif n > 7 :
            taken = n - 7
         elif n > 3 :
            taken = n - 3
         else : # ci sono certamente 2 biglie
            taken = 1
      else :
         taken = randint(1, n // 2)
      print("Biglie presenti nel mucchio:", n)
      print("Il computer ne ha prese:", taken)
      pile.take(taken) # eseguo la mossa
      

class NimGame :
   def __init__(self) :
      self._pile = NimPile(randint(10, 100))
      self._humanPlayer = NimHumanPlayer()
      self._computerPlayer = NimComputerPlayer(random() < 0.5)
      self._nextPlayer = self._humanPlayer if random() < 0.5 else self._computerPlayer
      
   def play(self) :
      while self._pile.getTotal() > 1 :
         self._nextPlayer.move(self._pile)
         self._nextPlayer = self._humanPlayer if self._nextPlayer == self._computerPlayer else self._computerPlayer
      if self._nextPlayer == self._computerPlayer :
         print("Hai vinto!")
      else :
         print("Il computer ha vinto: era ", end="")
         if self._computerPlayer.isExpert() :
            print("intelligente")
         else :
            print("stupido")

main()