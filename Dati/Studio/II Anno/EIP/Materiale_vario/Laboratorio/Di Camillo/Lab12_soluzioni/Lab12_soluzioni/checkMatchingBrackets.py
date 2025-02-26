# checkMatchingBrackets.py 

# osservare che se si fornisce allo standard input questo stesso
# file sorgente, che pure è sintatticamente corretto, vengono
# segnalati errori nelle parentesi... mentre con molti altri
# sorgenti Python la verifica funziona correttamente: perché?
# è evidente che le specifiche di questo "analizzatore sintattico"
# sono troppo semplificate per poter analizzare sorgenti Python...

from stackandqueue import *

def main() :
   """
      uso una pila per contenere, nell'ordine in cui sono state rilevate,
      tutte e sole le parentesi aperte (di qualsiasi tipo) per le quali non
      sia ancora stata trovata la corrispondente parentesi chiusa; all'inizio,
      ovviamente, la pila è vuota; il fatto di usare una pila consente di
      verificare correttamente l'annidamento tra parentesi di tipo diverso,
      nel senso che ([{}]) sarà corretto mentre ([{)}] non sarà corretto
      nonostante il numero di parentesi presenti sia corretto
   """
   pendingBrackets = Stack()
   lineNumber = 0 # servirà per la segnalazione d'errore
   while True :
      lineNumber += 1
      try :
         line = input()
      except EOFError :
         break
      for c in line :
         if isOpeningBracket(c) :
            pendingBrackets.push(c)
         elif isClosingBracket(c) :
            if len(pendingBrackets) == 0 \
                  or not areMatchingBrackets(pendingBrackets.pop(), c) :
               exit("Parentesi " + c + " erroneamente chiusa alla riga " + str(lineNumber))
         # else non devo fare niente perché non è una parentesi...
   if len(pendingBrackets) != 0 :
      exit("Non tutte le parentesi aperte sono state chiuse")
   print("Parentesi posizionate correttamente")
      
def isOpeningBracket(c) :
   return c == '(' or c == '[' or c == '{'
   
def isClosingBracket(c) :
   return c == ')' or c == ']' or c == '}'
   
def areMatchingBrackets(c1, c2) :
   return c1 == '(' and c2 == ')' or \
          c1 == '[' and c2 == ']' or \
          c1 == '{' and c2 == '}'

main()