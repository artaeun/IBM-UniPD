# standardDeviation.py
count = 0   # serve per fare la media e per segnalare errore se < 2
sum = 0
sumOfSquares = 0
print("Inserisci un numero per riga terminando con una riga vuota")
while True :
   s = input()
   if s == "" : break # riga vuota
   n = int(s)
   sum += n
   sumOfSquares += (n * n)
   count += 1
if count < 2 :
   print("Servono almeno due numeri")
else :
   print("Deviazione standard:", 
         ((sumOfSquares - (sum*sum)/count)/(count-1))**(1/2)) 