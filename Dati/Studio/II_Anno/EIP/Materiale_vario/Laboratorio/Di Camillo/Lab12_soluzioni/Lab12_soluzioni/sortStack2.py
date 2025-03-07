# sortStack2.py 

from stackandqueue import *

def main() :
   mess = "Fornire un numero intero positivo sulla riga di comando"
   from sys import argv, exit
   if len(argv) != 2 :
      exit(mess)
   try :
      size = int(argv[1])
   except ValueError :
      print(mess)
   if size <= 0 :
      print(mess)
   s = Stack()
   from random import random
   for i in range(size) :
      s.push(random())
   sortStackUsingOneStack(s)
   previous = s.top() # serve solo a far funzionare il primo test
   while len(s) != 0 :
      next = s.pop()
      if previous > next :
         exit("Collaudo fallito")
      print(next)
      previous = next
      
def sortStackUsingOneStack(s) :
   # invece di usare una seconda pila, usiamo s come pila temporanea,
   # ma dobbiamo sapere quanti sono gli elementi di s che costituiscono
   # la parte di memorizzazione temporanea, perché non possiamo vuotarla,
   # in quanto contiene anche la parte ordinata; in pratica, la parte "bassa"
   # di s contiene la pila che costituirà il risultato, mentre la parte "alta"
   # contiene, volta per volta, ciò che nella versione precedente era contenuto
   # nella pila temp2
   temp = Stack()
   toSort = len(s) # numero di elementi ancora da ordinare
   while len(s) != 0 :
      temp.push(s.pop())
   while toSort > 0 :
      max = temp.pop()
      toSort -= 1
      for i in range(toSort) :
         c = temp.pop()
         if c < max :
            s.push(c) # qui usavo temp2
         else :
            s.push(max)
            max = c
      # a questo punto i primi "toSort" elementi di s contengono
      # gli elementi che dovranno trovarsi in temp alla prossima
      # iterazione, cioè quelli da ordinare, mentre la parte bassa
      # di s contiene gli elementi già ordinati, che non devo
      # più spostare (sono len(s) - toSort - 1, poi inserirò max)
      for i in range(toSort) :
         temp.push(s.pop())
      s.push(max)

main()