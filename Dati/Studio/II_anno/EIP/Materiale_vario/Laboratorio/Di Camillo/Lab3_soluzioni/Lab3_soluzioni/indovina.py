# scrivere un programma che, dati 2 numeri interi a e b (a<b) in input,
# generi un numero intero casuale compreso tra a e b
# e chieda all'utente iterativamente (finché non indovina) di indovinare il valore del numero
# rispondendo ai tentativi con l'indicazione "Troppo piccolo!" o "Troppo grande!"
# Quando l'utente indovina il programma stampa a monitor il numero di tentativi fatti prima di indovinare
#
## Esempio di esecuzione:
## Scrivi il valore di a: 4
## Scrivi il valore di b: 14
## Indovina il numero: 10
## Troppo piccolo!
## Indovina il numero: 8
## Troppo piccolo!
## Indovina il numero: 7
## Troppo piccolo!
## Indovina il numero: 4
## Troppo grande!
## Indovina il numero: 5
## Hai indovinato in 5 mosse!



import random

smaller = int(input("Scrivi il valore di a: "))
larger = int(input("Scrivi il valore di b: "))
myNumber = random.randint(smaller, larger)
count = 0
while True:
    count += 1
    userNumber = int(input("Indovina il numero: "))
    if userNumber < myNumber:
        print("Troppo piccolo!")
    elif userNumber > myNumber:
        print("Troppo grande!")
    else:
        print("Hai indovinato in", count, "mosse!")
        break
