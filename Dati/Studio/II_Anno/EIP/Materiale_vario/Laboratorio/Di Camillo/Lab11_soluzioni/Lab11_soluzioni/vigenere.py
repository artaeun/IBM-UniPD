# vigenere.py
from sys import argv, exit

def main() :
   if len(argv) < 4 :
      exit("Parametri sulla riga di comando insufficienti")
   mode = argv[1]
   if mode != 'c' and mode != 'd' :
      exit("Il primo parametro deve essere c (cifratura) o d (decifrazione)")
   password = argv[3]
   if not password.isupper() or not password.isalpha() :
      exit("La password deve contenere soltanto lettere maiuscole")
   filename = argv[2]
   isURL1 = "http://"
   isURL2 = "https://"
   if filename.startswith(isURL1) or filename.startswith(isURL2) :
      from urllib.request import urlopen
      webPage = urlopen(filename)
      text = str(webPage.read(), "utf-8")
      webPage.close()
   else :
      try :
         f = open(filename, "r")
      except FileNotFoundError :
         exit("File %s non accessibile" % filename)
      text = f.read()
      f.close() 
   paramSign = 1      
   if mode == 'd' :
      paramSign = -1
   i = 0
   for c in text : 
      print(caesarCode(paramSign*(ord(password[i]) - ord('A')), c), end="")
      i = (i + 1) % len(password)      
         
def caesarCode(param, c) : # ok anche con param negativo
   if c >= 'A' and c <= 'Z' :
      return chr(ord('A') + (ord(c) - ord('A') + param) % (ord('z')-ord('a')+1))
   if c >= 'a' and c <= 'z' :
      return chr(ord('a') + (ord(c) - ord('a') + param) % (ord('z')-ord('a')+1))
   return c
   
main()