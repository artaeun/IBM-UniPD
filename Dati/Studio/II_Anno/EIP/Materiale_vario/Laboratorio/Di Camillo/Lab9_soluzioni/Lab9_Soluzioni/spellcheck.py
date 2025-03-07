# spellcheck.py
import os, os.path
from urllib.request import urlopen
from re import split

def main() :
   filename = input("File da controllare (oppure URL di Internet): ")
   if len(filename) == 0 :
      filename = "http://www.gutenberg.org/cache/epub/4357/pg4357.txt"
   dictname = input("File dizionario (oppure URL di Internet): ")
   if len(dictname) == 0 :
      dictname = "https://users.cs.duke.edu/~ola/ap/linuxwords"
   isURL1 = "http://"
   isURL2 = "https://"
   if filename.startswith(isURL1) or filename.startswith(isURL2) :
      webPage = urlopen(filename)
      text = str(webPage.read(), "utf-8")
      webPage.close()
   else :
      f = open(filename, "r")
      text = f.read()
      f.close()
   if dictname.startswith(isURL1) or dictname.startswith(isURL2) :
      webPage = urlopen(dictname)
      dictText = str(webPage.read(), "utf-8")
      webPage.close()
   else :
      f = open(dictname, "r")
      dictText = f.read()
      f.close()
   dictWords = dictText.lower().splitlines()
   words = split("[^a-z]+", text.lower())
   words.sort()
   uniqueWords = []
   for i in range(1, len(words)) :
      if words[i] != words[i-1] :
         uniqueWords.append(words[i])
   for word in uniqueWords :
      if word not in dictWords :
         print(word)
   
main()
