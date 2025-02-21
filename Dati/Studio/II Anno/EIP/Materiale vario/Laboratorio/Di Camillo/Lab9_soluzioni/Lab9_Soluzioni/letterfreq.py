# letterfreq.py

def main() :
   filename = input("File da controllare (oppure URL di Internet): ")
   if len(filename) == 0 :
      filename = "http://www.gutenberg.org/cache/epub/4357/pg4357.txt"
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
   text = text.lower()
   count = 0
   counts = [0] * (ord('z') - ord('a') + 1)
   for c in text :
      if c >= 'a' and c <= 'z' :
         count += 1
         counts[ord(c) - ord('a')] += 1
   for c in range(ord('a'), ord('z') + 1) :
      print(chr(c) + ("%6.2f" % (100*counts[c - ord('a')] / count)))
   
main()
