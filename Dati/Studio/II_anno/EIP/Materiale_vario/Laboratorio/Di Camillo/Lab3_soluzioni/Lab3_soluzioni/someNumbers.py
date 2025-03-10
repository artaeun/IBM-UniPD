# someNumbers.py
count = 0   # serve per fare la media e per segnalare errore se < 2
sum = 0
sumOfAbs = 0
product = 1 # attenzione all'inizializzazione del prodotto... non zero!
print("Inserisci un numero per riga terminando con una riga vuota")
while True :
   s = input()
   if s == "" : break # riga vuota
   n = int(s)
   sum += n
   sumOfAbs += abs(n)
   product *= n
   count += 1
if count < 2 :
   print("Servono almeno due numeri")
else :
   print("Somma:", sum)
   print("Somma dei valori assoluti:", sumOfAbs)
   print("Prodotto:", product)
   print("Valore medio:", (sum / count)) # le parentesi interne non sono necessarie