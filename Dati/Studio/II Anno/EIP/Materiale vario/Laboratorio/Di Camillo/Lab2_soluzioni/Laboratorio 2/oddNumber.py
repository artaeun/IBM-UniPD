# oddNumber.py
#
# definisco il messaggio in una variabile perché lo userò più volte,
# così sono sicuro che sarà identico
message = "Scrivi un numero dispari: "
odd = int(input(message))
if odd % 2 == 0 :
   print("Ho detto dispari! Riprova")
   odd = int(input(message))
if odd % 2 == 0 :
   print("Ripassa il concetto di numero dispari, ti saluto.")
else :
   print("Complimenti! Il numero", odd, "è dispari!")