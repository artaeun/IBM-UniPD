# guessNumber.py
from random import randint
from sys import exit
smaller = int(input("Valore di a, numero intero positivo: "))
larger = int(input("Valore di b, numero intero maggiore di a: "))
if (not (0 < smaller < larger)) :
   exit("Valori errati")
toGuess = randint(smaller, larger)
count = 0
while True:
    count += 1
    guess = int(input("Indovina il numero: "))
    if guess < toGuess:
        print("Troppo piccolo!")
    elif guess > toGuess:
        print("Troppo grande!")
    else:
        print("Hai indovinato in", count, "mosse!")
        break