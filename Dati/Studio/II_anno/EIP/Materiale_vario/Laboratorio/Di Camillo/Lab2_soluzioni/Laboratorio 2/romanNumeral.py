# romanNumeral.py
n = int(input("Numero intero da convertire in numero romano (da 1 a 3999) "))
if n > 0 and n < 4000 :
   roman = ""
   thou = n // 1000
   if thou == 1 :
      roman = roman + "M"
   elif thou == 2 :
      roman = roman + "MM"
   elif thou == 3 :
      roman = roman + "MMM"
   hund = (n - thou * 1000) // 100
   if hund == 1 :
      roman = roman + "C"
   elif hund == 2 :
      roman = roman + "CC"
   elif hund == 3 :
      roman = roman + "CCC"
   elif hund == 4 :
      roman = roman + "CD"
   elif hund == 5 :
      roman = roman + "D"
   elif hund == 6 :
      roman = roman + "DC"
   elif hund == 7 :
      roman = roman + "DCC"
   elif hund == 8 :
      roman = roman + "DCCC"
   elif hund == 9 :
      roman = roman + "CM"
   tens = (n - thou * 1000 - hund * 100) // 10
   if tens == 1 :
      roman = roman + "X"
   elif tens == 2 :
      roman = roman + "XX"
   elif tens == 3 :
      roman = roman + "XXX"
   elif tens == 4 :
      roman = roman + "XL"
   elif tens == 5 :
      roman = roman + "L"
   elif tens == 6 :
      roman = roman + "LX"
   elif tens == 7 :
      roman = roman + "LXX"
   elif tens == 8 :
      roman = roman + "LXXX"
   elif tens == 9 :
      roman = roman + "XC"
   units = n - thou * 1000 - hund * 100 - tens * 10
   if units == 1 :
      roman = roman + "I"
   elif units == 2 :
      roman = roman + "II"
   elif units == 3 :
      roman = roman + "III"
   elif units == 4 :
      roman = roman + "IV"
   elif units == 5 :
      roman = roman + "V"
   elif units == 6 :
      roman = roman + "VI"
   elif units == 7 :
      roman = roman + "VII"
   elif units == 8 :
      roman = roman + "VIII"
   elif units == 9 :
      roman = roman + "IX"
   print(roman)
else :
   print("Numero errato")