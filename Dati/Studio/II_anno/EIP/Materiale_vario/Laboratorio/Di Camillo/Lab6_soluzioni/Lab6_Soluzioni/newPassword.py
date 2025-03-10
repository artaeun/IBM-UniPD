# newPassword.py
def main() :
   while True :
      s = input("Password: ")
      if isValid(s) :
         print("OK")
         break
      print("Inserire una nuova password")

def isValid(password) :
   ok = True
   if not rule1(password) :
      ok = False
      print("La password non contiene almeno 8 caratteri")
   if not rule2(password) :
      ok = False
      print("La password non ha almeno una lettera maiuscola")
   if not rule3(password) :
      ok = False
      print("La password non ha almeno una lettera minuscola")
   if not rule4(password) :
      ok = False
      print("La password non ha almeno una cifra numerica")
   if not rule5(password) :
      ok = False
      print("La password non ha almeno un carattere che non sia una lettera né una cifra")
   if not rule6(password) :
      ok = False
      print("La password contiene almeno uno spazio")
   if not rule7(password) :
      ok = False
      print("La password contiene almeno un carattere ripetuto")
   return ok

def rule1(password) :
   return len(password) >= 8
   
def rule2(password) :
   return password != password.lower()
   
def rule3(password) :
   return password != password.upper()
   
def rule4(password) :
   for char in password :
      if char.isdigit() : 
         return True
   return False
   
def rule5(password) :
   for char in password :
      if not char.isalnum() :
         return True
   return False
   
def rule6(password) :
   for char in password :
      if char == ' ' :
         return False
   return True

def rule7(password) :
   for i in range(len(password)) :
      for j in range(i + 1, len(password)) :
         if password[i] == password[j] :
            return False
   return True

main()