# numberName.py
from myinput import *
from sys import exit

def main() :
   n = inputPositiveDecimalInteger("Numero intero positivo minore di un milione: ")
   if n >= 1_000_000 : # notare l'uso di _ per separare le migliaia: è ammesso
      exit("Numero troppo grande!")
   s = ""
   # 1 <= n <= 999999
   thousands = n // 1000
   # 1 <= thousands <= 999
   if thousands > 1 :
      s += upTo999(thousands)
      s += "mila"
   elif thousands == 1 :
      s += "mille"
   x = n % 1000
   # 1 <= x <= 999
   s += upTo999(x)
   if n % 10 == 3 and n != 3 :
      s = s[:-1] + "é"
   print(s)
   
def upTo999(n) :
   s = ""
   hundreds = n // 100
   # 1 <= hundreds <= 9
   if hundreds > 1 :
      s += upTo9(hundreds)
   if hundreds >= 1 :
      s += "cento"
   n = n % 100
   # 1 <= n <= 99
   s += upTo99(n)
   return s

def upTo99(n) :
   if n <= 9 : return upTo9(n)
   if n == 10 : return "dieci"
   if n == 11 : return "undici"
   if n == 12 : return "dodici"
   if n == 13 : return "tredici"
   if n == 14 : return "quattordici"
   if n == 15 : return "quindici"
   if n == 16 : return "sedici"
   if n == 17 : return "diciassette"
   if n == 18 : return "diciotto"
   if n == 19 : return "diciannove"
   tens = n // 10
   # 2 <= tens <= 9
   if tens == 2 : s = "venti"
   elif tens == 3 : s = "trenta"
   elif tens == 4 : s = "quaranta"
   elif tens == 5 : s = "cinquanta"
   elif tens == 6 : s = "sessanta"
   elif tens == 7 : s = "settanta"
   elif tens == 8 : s = "ottanta"
   elif tens == 9 : s = "novanta"
   units = upTo9(n % 10)
   if units == "uno" or units == "otto" :
      s = s[:-1] # tolgo la vocale finale delle decine
   return s + units
   
   
def upTo9(n) :
   if n == 1 : return "uno"
   if n == 2 : return "due"
   if n == 3 : return "tre"
   if n == 4 : return "quattro"
   if n == 5 : return "cinque"
   if n == 6 : return "sei"
   if n == 7 : return "sette"
   if n == 8 : return "otto"
   if n == 9 : return "nove"
   return ""
   
main()