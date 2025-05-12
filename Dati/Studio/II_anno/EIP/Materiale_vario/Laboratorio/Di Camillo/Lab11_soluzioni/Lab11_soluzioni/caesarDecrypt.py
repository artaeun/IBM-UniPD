# caesarDecrypt.py
from sys import argv, exit

def main() :
   if len(argv) < 2 :
      exit()
   filename = argv[1]
   isURL1 = "http://"
   isURL2 = "https://"
   if filename.startswith(isURL1) or filename.startswith(isURL2) :
      from urllib.request import urlopen
      webPage = urlopen(filename)
      text = str(webPage.read(), "utf-8")
      webPage.close()
   else :
      f = open(filename, "r")
      text = f.read()
      f.close()
   param = 3
   if len(argv) > 2 :
      try :
         x = int(argv[2])
         if x > 0 : # altrimenti ignoro
            param = x
      except ValueError :
         pass # ignoro      
   for c in text :
      if c >= 'A' and c <= 'Z' :
         print(chr(ord('A') + (ord(c) - ord('A') - param) % (ord('z')-ord('a')+1)), end="")
      elif c >= 'a' and c <= 'z' :
         print(chr(ord('a') + (ord(c) - ord('a') - param) % (ord('z')-ord('a')+1)), end="")
      else :
         print(c, end="")
   
main()
