# findEmptyDir.py
import os, os.path

def main() :
   dir = input("Cartella da cui iniziare la ricerca: ")
   if len(dir) == 0 :
      dir = os.getcwd()
   findEmptyDir(dir)
   
def findEmptyDir(dir) :
   if os.path.isdir(dir) :
      if len(os.listdir(dir)) == 0 :
         print(dir)
      else : 
         for name in os.listdir(dir):
            findEmptyDir(dir + os.sep + name)        

main()
