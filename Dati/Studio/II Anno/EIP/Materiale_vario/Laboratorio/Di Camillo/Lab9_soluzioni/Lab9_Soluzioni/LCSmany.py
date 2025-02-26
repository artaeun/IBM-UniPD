# LCSmany.py

def main() :
   ss = []
   while True :
      s = input()
      if len(s) == 0 :
         break
      ss.append(s)
   if len(ss) > 1 : # con meno di due stringhe non c'è niente da calcolare...
      print("LCS:", LCSmany(ss))

def LCSmany(ss) :
   # se almeno una delle stringhe è vuota,
   # non ci possono essere caratteri comuni a tutte le stringhe
   for s in ss :
      if len(s) == 0 :
         return ""
   # considero il primo carattere di tutte le stringhe:
   # se tutte le stringhe hanno il primo carattere in comune,
   # la più lunga sottosequenza comune sarà composta da tale
   # carattere seguito dalla più lunga sottosequenza comune
   # alle parti rimanenti delle stringhe, da cui ho eliminato
   # il primo carattere
   c = ss[0][0] # primo carattere della prima stringa
   k = 0
   for s in ss :
      if s[0] == c :
         k += 1
      else :
         break # ho trovato una stringa che inizia diversamente
   if k == len(ss) :
      # iniziano tutte con lo stesso carattere
      sss = [] # creo la nuova lista di stringhe
      for s in ss :
         sss.append(s[1:]) # inserisco tutte le stringhe private del primo carattere
      return c + LCSmany(sss)
   # i caratteri iniziali non sono tutti uguali, quindi calcolo la
   # più lunga sottosequenza comune in più insiemi di stringhe, ciascuno
   # ottenuto considerando tutte le stringhe originali tranne una, alla
   # quale viene eliminato il primo carattere; la stringa da cui elimino
   # il carattere è sempre diversa
   max = "" # sarà il risultato
   for i in range(len(ss)) :
      sss = list(ss) # clono la lista
      sss[i] = ss[i][1:] # sostituisco una stringa con se stessa privata del primo carattere
      s = LCSmany(sss)
      if len(s) > len(max) :
         max = s # ho trovato una sottosequenza più lunga
   # restituisco la stringa più lunga fra quelle calcolate
   return max

main()