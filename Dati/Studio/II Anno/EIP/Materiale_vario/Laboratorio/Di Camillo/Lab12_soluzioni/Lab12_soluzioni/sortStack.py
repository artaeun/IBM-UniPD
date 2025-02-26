# sortStack.py 

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
   sortStackUsingTwoStacks(s)
   previous = s.top() # serve solo a far funzionare il primo test
   while len(s) != 0 :
      next = s.pop()
      if previous > next :
         exit("Collaudo fallito")
      print(next)
      previous = next
      
def sortStackUsingTwoStacks(s) :
   temp1 = Stack()
   while len(s) != 0 :
      temp1.push(s.pop())
   temp2 = Stack()
   while len(temp1) != 0 :
      # svuoto temp1 cercando il suo valore massimo
      # mentre svuoto temp1, trasferisco i suoi elementi in temp2,
      # evitando però di inserire in temp2 il valore massimo
      max = temp1.pop() # attuale candidato a essere il massimo
      while len(temp1) != 0 :
         c = temp1.pop()
         if c < max :
            temp2.push(c)
         else :
            # max non è più candidato a essere il massimo,
            # quindi lo inserisco in temp2
            temp2.push(max)
            max = c
      # ora max contiene il valore massimo che era presente in 
      # temp1 (che è rimasta vuota), mentre temp2 contiene tutti
      # i valori che erano in temp1 tranne max, quindi impilo max
      # nella pila s che conterrà il risultato
      s.push(max)
      # a questo punto per proseguire dovrei svuotare temp2,
      # inserendo in temp1 tutti i suoi elementi, ma per ottenere
      # lo stesso risultato basta scambiare i riferimenti!
      (temp1, temp2) = (temp2, temp1)
      # ora temp2 punta a una pila vuota e temp1 punta a una pila
      # che contiene i valori ancora da elaborare
      # DECISAMENTE più veloce... considerando che risparmio questa
      # copiatura a ogni iterazione del ciclo... se la pila conteneva
      # un milione di elementi, la prima volta risparmio un milione
      # di trasferimenti, la seconda volta ne risparmio 999999...
      # in pratica il risparmio è la somma dei primi "size" numeri
      # interi, una quantità quadratica in funzione di size
   # osservo che se s è una pila vuota non c'è bisogno di
   # una gestione separata: l'algoritmo funziona correttamente

main()