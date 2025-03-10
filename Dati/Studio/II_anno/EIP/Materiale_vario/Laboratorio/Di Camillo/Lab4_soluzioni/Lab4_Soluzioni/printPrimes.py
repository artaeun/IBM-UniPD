# printPrimes.py
while True :
   maxValue = int(input("Inserisci il valore massimo, intero maggiore di uno: "))
   if maxValue > 1 :
      break
print("Numeri primi non maggiori di " + str(maxValue) + ":")
i = 2
while i <= maxValue :
   isPrime = True
   """
      Domanda:
      nel ciclo sottostante, è veramente necessario
      imporre la condizione j < i, oppure si potrebbe
      usare un vincolo più restrittivo
      (cioè j < di una quantità minore di i) ???
   """
   j = 2
   while j < i and isPrime :
      if i % j == 0 :
         isPrime = False
      j += 1
   if isPrime :
      print(i)
   i += 1