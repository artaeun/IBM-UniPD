# recursiveAndIterativeFibonacci.py
from myinput import inputDecimalInteger
from time import perf_counter

def main() :
   while True :
      n = inputDecimalInteger("Numero intero non negativo: ")
      if n >= 0 :
         break
   beginTimeIter = perf_counter()
   iterFib = iterativeFib(n)
   timeIter = perf_counter() - beginTimeIter
   beginTimeRecur = perf_counter()
   recurFib = recursiveFib(n)
   timeRecur = perf_counter() - beginTimeRecur
   if iterFib != recurFib :
      print("ERRORE")
   else :
       print("Il numero di Fibonacci di ordine %i è %i" % (n, iterFib))
       print("Tempo per il calcolo iterativo (in secondi): %.3f" % timeIter)
       print("Tempo per il calcolo ricorsivo (in secondi): %.3f" % timeRecur)
  
def iterativeFib(n) :
   if n < 2 : # in realtà basterebbe n < 1
      return n 
   fib0 = 0
   fib1 = 1
   for i in range(2, n+1) :
      newFib = fib0 + fib1
      fib0 = fib1
      fib1 = newFib
   return fib1

def recursiveFib(n) :
   if n < 2 : # casi base
      return n
   return recursiveFib(n-2) + recursiveFib(n-1)
   
main()