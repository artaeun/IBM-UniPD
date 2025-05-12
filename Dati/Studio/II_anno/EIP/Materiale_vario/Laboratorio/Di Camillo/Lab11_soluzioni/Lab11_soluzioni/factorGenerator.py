# factorGenerator.py (modulo)

"""
   La difficoltà principale dell'esercizio consiste nell'individuazione
   delle informazioni di stato sufficienti al funzionamento del
   fattorizzatore. L'esercizio può, ovviamente, essere risolto in
   modi diversi, l'idea su cui si basa questa soluzione è la
   seguente:
   *) inizialmente, il numero da scomporre è quello ricevuto dal
      costruttore
   *) quando viene richiesto un fattore, lo si calcola; dopodiché si memorizza,
      come numero ancora da scomporre, il quoziente tra il numero
      precedentemente da scomporre e il fattore che si sta per
      restituire: questa è l'informazione necessaria e sufficiente
      per proseguire (ad esempio, è inutile ricordarsi il numero
      originario, così come è inutile ricordarsi i fattori già
      restituiti)
   *) quando il numero (che è rimasto) da fattorizzare è uguale a 1,
      significa che la scomposizione è terminata: questa proprietà
      viene sfruttata dal metodo hasMoreFactors()
"""

class FactorGenerator :

   def __init__(self, toFactorize) :
      if not isinstance(toFactorize, int) or toFactorize < 2 :
         raise ValueError
      self._toFactorize = toFactorize
      
   def hasMoreFactors(self) :
      return self._toFactorize > 1
      
   def nextFactor(self) :
      if self._toFactorize == 1 :
         raise StopIteration
      """
         cercando i divisori in ordine crescente, un eventuale
         divisore è certamente primo: se così non fosse, si
         sarebbe trovato prima di esso un suo divisore che
         sarebbe stato anche divisore di self._toFactorize;
         esempio: se self._toFactorize è divisibile per 4 (che non è primo)
         l'algoritmo trova prima il divisore 2 (che, essendo
         divisore di 4, è certamente anche divisore di self._toFactorize),
         lo restituisce e, la volta successiva, verrà nuovamente
         trovato il divisore 2, come deve essere, dato che self._toFactorize
         era divisibile per 4 = 2 * 2
         quindi, anche se non era richiesto, il metodo restituisce i fattori
         in ordine crescente, perché è più comodo individuarli in tale ordine
      """
      i = 2
      while i <= self._toFactorize : # il segno uguale serve quando il numero è primo:
                                     # in tal caso il suo unico divisore è il numero stesso
         if self._toFactorize % i == 0 :
            # self._toFactorize è divisibile per i
            self._toFactorize //= i
            # ora self._toFactorize contiene il numero che rimane da scomporre
            return i
         else :
            i += 1

if __name__ == "__main__" :
   from myinput import *
   while True :
      num = inputPositiveDecimalInteger("Numero intero da scomporre: ")
      if num > 1 :
         break
   f = FactorGenerator(num)
   while f.hasMoreFactors() :
      print(f.nextFactor())
   # nel collaudo, verifico che a questo punto un'ulteriore invocazione
   # di nextFactor sollevi l'eccezione prevista
   try :
      f.nextFactor()
   except StopIteration :
      print("OK")