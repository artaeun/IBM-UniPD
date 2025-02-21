# isLeapYear.py
year = int(input("Inserisci l'anno (numero intero positivo): "))
if year <= 0 :
   print("Il numero inserito non e' positivo")
else :
   isLeap = False # di solito non è bisestile...
   if year % 4 == 0 : # forse è bisestile...
      if  year < 1582 : # non c'erano eccezioni, è bisestile
         isLeap = True
      else : # controllo le eccezioni
         if year % 100 != 0 :
            isLeap = True # non divisibile per 100, quindi bisestile
         else :
            if year % 400 == 0 : # divisibile per 400, quindi bisestile
               isLeap = True
               """
                  qui non serve else perché se non è divisibile per 400
                  (ma è divisibile per 100, dato che sono qui...)
                  allora NON è bisestile, ma per segnalare che non è
                  bisestile non devo fare niente, la variabile booleana
                  isLeap ha gia' il valore corretto
               """

   message = "L'anno " + str(year) + " "
   if isLeap == False :
      message = message + "non "
   message = message + "è bisestile"
   print(message)