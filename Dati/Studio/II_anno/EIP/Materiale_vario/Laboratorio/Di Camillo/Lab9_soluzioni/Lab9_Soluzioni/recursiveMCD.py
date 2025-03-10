# recursiveMCD.py
from myinput import inputPositiveDecimalInteger

def main() :
   n1 = inputPositiveDecimalInteger("Primo numero intero positivo: ")
   n2 = inputPositiveDecimalInteger("Secondo numero intero positivo: ")
   mcd = recursiveMCD(n1, n2)
   print("Il massimo comun divisore di %i e %i è %i" % (n1, n2, mcd))
  
def recursiveMCD(m, n) :
   if m % n == 0 :
      return n
   return recursiveMCD(n, m % n)
   
main()