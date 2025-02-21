# findFile.py
import os, os.path

def main() :
   search = input("Stringa da cercare: ")
   dir = input("Cartella da cui iniziare la ricerca: ")
   if len(dir) == 0 :
      dir = os.getcwd()
   findFile(dir, search)
   
def findFile(dir, search) :
   if os.path.isdir(dir) :
      names = os.listdir(dir)
      for name in names :
         if os.path.isfile(dir + os.sep + name) :
            if search in name :
               print(dir + os.sep + name)
         else : # è una cartella
            findFile(dir + os.sep + name, search)        

main()
