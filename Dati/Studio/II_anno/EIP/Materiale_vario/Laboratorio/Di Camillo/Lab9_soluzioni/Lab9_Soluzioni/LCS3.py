# LCS3.py

def main() :
   s1 = input("Prima stringa: ")
   s2 = input("Seconda stringa: ")
   s3 = input("Terza stringa: ")
   print("LCS:", LCS3(s1, s2, s3))

def LCS3(s1, s2, s3) :
   # se almeno una delle stringhe è vuota,
   # non ci possono essere caratteri comuni alle due stringhe
   # quindi LCS è la stringa vuota
   if len(s1) == 0 or len(s2) == 0 or len(s3) == 0 :
      return ""
   # considero il primo carattere delle tre stringhe:
   # se le tre stringhe hanno il primo carattere in comune,
   # la più lunga sottosequenza comune sarà composta da tale
   # carattere seguito dalla più lunga sottosequenza comune
   # alle parti rimanenti delle stringhe, da cui ho eliminato
   # il primo carattere
   if s1[0] == s2[0] == s3[0] :
      return s1[0] + LCS3(s1[1:], s2[1:], s3[1:])
   # i caratteri iniziali sono diversi, quindi calcolo la
   # più lunga sottosequenza comune alla parte rimanente della prima
   # stringa (senza il suo primo carattere) e alle altre due stringhe intere;
   # poi, ripeto il calcolo variando la stringa che "perde" il primo carattere,
   # negli altri due modi possibili
   sub1 = LCS3(s1[1:], s2, s3)
   sub2 = LCS3(s1, s2[1:], s3)
   sub3 = LCS3(s1, s2, s3[1:])
   # infine restituisco la stringa più lunga fra quelle calcolate
   maxlen = max(len(sub1), len(sub2), len(sub3))
   if len(sub1) == maxlen :
      return sub1
   if len(sub2) == maxlen :
      return sub2
   return sub3

main()