# LCS2.py

def main() :
   s1 = input("Prima stringa: ")
   s2 = input("Seconda stringa: ")
   print("LCS:", LCS2(s1, s2))

def LCS2(s1, s2) :
   # se almeno una delle stringhe è vuota,
   # non ci possono essere caratteri comuni alle due stringhe
   # quindi LCS è la stringa vuota
   if len(s1) == 0 or len(s2) == 0 :
      return ""
   # considero il primo carattere delle due stringhe:
   # se le due stringhe hanno il primo carattere in comune,
   # la più lunga sottosequenza comune sarà composta da tale
   # carattere seguito dalla più lunga sottosequenza comune
   # alle parti rimanenti delle stringhe, da cui ho eliminato
   # il primo carattere
   if s1[0] == s2[0] :
      return s1[0] + LCS2(s1[1:], s2[1:])
   # i caratteri iniziali sono diversi, quindi calcolo la
   # più lunga sottosequenza comune alla parte rimanente della prima
   # stringa (senza il suo primo carattere) e alla seconda stringa intera;
   # poi calcolo la più lunga sottosequenza comune alla prima stringa intera
   # e alla parte rimanente della seconda stringa (senza il suo primo carattere)
   sub1 = LCS2(s1[1:], s2)
   sub2 = LCS2(s1, s2[1:])
   # infine restituisco la stringa più lunga fra quelle calcolate
   if len(sub1) > len(sub2) :
      return sub1
   return sub2

main()