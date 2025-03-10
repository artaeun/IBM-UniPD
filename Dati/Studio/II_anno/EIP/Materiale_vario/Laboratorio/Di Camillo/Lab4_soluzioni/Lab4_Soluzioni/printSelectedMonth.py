# printSelectedMonth.py
months = ""
months += "Gennaio  "
oneMonthLength = len(months)
months += "Febbraio "
months += "Marzo    "
months += "Aprile   "
months += "Maggio   "
months += "Giugno   "
months += "Luglio   "
months += "Agosto   "
months += "Settembre"
months += "Ottobre  "
months += "Novembre "
months += "Dicembre " # stringhe aventi tutte la stessa lunghezza...
                      # questo e' il "trucco" che fa funzionare il programma!
month = int(input("Inserisci il numero del mese (1-12): "))
begin = (month - 1) * oneMonthLength
selectedMonth = months[begin : begin + oneMonthLength]
print(selectedMonth)
