# myinput.py (modulo)

def inputYesNo(message, yes, no) :
   while True :
      s = input(message)
      if s == yes :
         return True
      if s == no :
         return False

def inputStringStartingWith(message, startingString) :
   while True :
      s = input(message)
      if s.startswith(startingString) :
         return s

def inputStringEndingWith(message, endingString) :
   while True :
      s = input(message)
      if s.endswith(endingString) :
         return s

def inputStringContaining(message, substring) :
   while True :
      s = input(message)
      if substring in s :
         return s
         
def isDecimalInteger(s) :
   atLeastOneDigit = False
   i = 0
   while i < len(s) : # spazi iniziali ?
      if s[i] != ' ' :
         break
      i += 1 # il valore finale di i corrisponde al primo carattere
             # della stringa che NON è uno spazio (eventualmente zero)
   if i < len(s) and s[i] == '-' : # segno meno ?
      i += 1
   while i < len(s) : # cifre decimali ?
      if not s[i].isdigit() :
         break
      atLeastOneDigit = True
      i += 1
   while i < len(s) : # spazi finali ?
      if s[i] != ' ' :
         break
      i += 1
   # se i == len(s) vuol dire che sono riuscito a scandire tutta
   # la stringa rispettando il formato, devo solo controllare che
   # ci sia almeno una cifra numerica (potrebbero essere tutti spazi)
   return i == len(s) and atLeastOneDigit 
   # osservate bene l'istruzione qui sopra... quando si deve eseguire
   # una cosa come questa
   #
   #    if condizione :
   #       return True
   #    else:
   #       return False
   #
   # si può semplicemente scrivere
   #
   #    return condizione
   #
   # perché? capire...
   # analogamente, al posto di
   #
   #    if condizione :
   #       variabile = True
   #    else :
   #       variabile = False
   #
   # si può scrivere
   #
   #    variabile = condizione

def inputDecimalInteger(message) :
   while True :
      s = input(message)
      if isDecimalInteger(s) : # sicuramente int(s) non fallirà
         return int(s)
         
def inputPositiveDecimalInteger(message) :
   while True :
      n = inputDecimalInteger(message)
      if n > 0 :
         return n
         
def inputNegativeDecimalInteger(message) :
   while True :
      n = inputDecimalInteger(message)
      if n < 0 :
         return n

def inputNonPositiveDecimalInteger(message) :
   while True :
      n = inputDecimalInteger(message)
      if n <= 0 :
         return n
         
def inputNonNegativeDecimalInteger(message) :
   while True :
      n = inputDecimalInteger(message)
      if n >= 0 :
         return n

def isFloating(s) :
   atLeastOneDigit = False
   i = 0
   while i < len(s) : # spazi iniziali ?
      if s[i] != ' ' :
         break
      i += 1 # il valore finale di i corrisponde al primo carattere
             # della stringa che NON è uno spazio (eventualmente zero)
   if i < len(s) and s[i] == '-' : # segno meno ?
      i += 1
   while i < len(s) : # cifre decimali della parte intera ?
      if not s[i].isdigit() :
         break
      atLeastOneDigit = True
      i += 1
   if i < len(s) and s[i] == '.' : # separatore decimale ?
      i += 1
   while i < len(s) : # cifre decimali della parte frazionaria ?
      if not s[i].isdigit() :
         break
      atLeastOneDigit = True
      i += 1
   # parte esponenziale facoltativa...
   eLetterIsPresent = False
   atLeastOneExponentDigit = False
   if i < len(s) and s[i].upper() == 'E' : # lettera "e" maiuscola o minuscola ?
      eLetterIsPresent = True
      i += 1
      if i < len(s) and s[i] == '-' : # segno meno dell'esponente ?
         i += 1
      while i < len(s) : # cifre decimali dell'esponente ?
         if not s[i].isdigit() :
            break
         atLeastOneExponentDigit = True
         i += 1
   while i < len(s) : # spazi finali ?
      if s[i] != ' ' :
         break
      i += 1      
   return i == len(s) and atLeastOneDigit \
          and (eLetterIsPresent == atLeastOneExponentDigit)      
         
def inputFloating(message) :
   while True :
      s = input(message)
      if isFloating(s) : # sicuramente float(s) non fallirà
         return float(s)