# checkCircles.py
x1 = float(input("Circonferenza 1 - Centro x: "))
y1 = float(input("Circonferenza 1 - Centro y: "))
r1 = float(input("Circonferenza 1 - Raggio: "))
x2 = float(input("Circonferenza 2 - Centro x: "))
y2 = float(input("Circonferenza 2 - Centro y: "))
r2 = float(input("Circonferenza 2 - Raggio: "))
if r1 <= 0 or r2 <= 0 :
   print("Errore: entrambi i raggi devono essere positivi")
else :
   # calcolo la distanza tra i centri (teorema di Pitagora...)
   d = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
   # calcolo il valore assoluto della differenza tra i raggi
   diff = r1 - r2
   if diff < 0 :
      diff = -diff
   # calcolo la somma dei raggi
   sum = r1 + r2
   # alternative multiple per decidere...
   if d == 0 :
      if r1 == r2 : # qui è vero che d == 0 and r1 == r2
         print("Le due circonferenze sono coincidenti")
      else :        # qui è vero che d == 0 and r1 != r2
         print("Le due circonferenze sono concentriche (ma non coincidenti)")
   elif 0 < d < diff :
      print("Le due circonferenze sono una interna all'altra, ma non concentriche")
   elif d == diff :
      print("Le due circonferenze sono tangenti internamente")
   elif diff < d < sum :
      print("Le due circonferenze sono secanti")
   elif d == sum :
      print("Le due circonferenze sono tangenti esternamente")
   else : # qui è vero che d > sum, non c'è bisogno di verificarlo
      print("Le due circonferenze sono (reciprocamente) esterne")