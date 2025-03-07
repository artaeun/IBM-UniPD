# fileCompare.py
from sys import argv, exit

def main() :
   if len(argv) < 3 :
      exit()
   try :
      f1 = open(argv[1], "r")
      f2 = open(argv[2], "r")
   except FileNotFoundError :
      exit()
   if f1.read() != f2.read() :
      print("I file sono diversi")
   f1.close()
   f2.close()
   
main()
