# isPrime.py
from myinput import *
from factorGenerator import FactorGenerator
while True :
   num = inputPositiveDecimalInteger("Potenziale numero primo: ")
   if num > 1 :
      break
f = FactorGenerator(num)
# il numero num è primo
# se e solo se il primo fattore restituito da nextFactor è il numero stesso
if f.nextFactor() == num :
   print("Il numero %d è primo" % num)
else :
   print("Il numero %d non è primo" % num)