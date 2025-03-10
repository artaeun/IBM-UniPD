# maze3.py

from sys import exit

def main() :
   m = Maze((10, 15, 0.1, 0.1, 4))
   #m = Maze("maze.txt")
   print(m)
   m.help()
   m.findRoute()
   print(m)

class Maze :

   OK = " "
   WALL = "*"
   UNKNOWNDIR = "?"
   START = "#"
   ROUTE = "+"
   
   def __init__(self, x) :
      if isinstance(x, str) :
         self._readFromFile(x) # uso un metodo privato per chiarezza
      elif isinstance(x, tuple) :
         self._generate(x)     # uso un metodo privato per chiarezza
      else :
         raise TypeError("Errore nei parametri di costruzione")
         
   def _generate(self, params) : # metodo privato
      self._width = width = params[0]
      self._height = height = params[1]
      holesPercent = params[2]
      wallPercent = params[3]
      wallMaxLength = params[4]
      from random import random, randint
      self._lines = lines = list()
      # genero il muro perimetrale
      lines.append(Maze.WALL * width + "\n")
      for i in range(height - 2) :
         lines.append(Maze.WALL + (Maze.OK * (width - 2)) + Maze.WALL + "\n")
      lines.append(Maze.WALL * width + "\n")
      # genero i varchi nel muro perimetrale, controllando che ne venga
      # generato almeno uno... evitando di generare varchi negli angoli
      count = 0
      for i in range(1, width - 1) : # inutile generare un varco in un angolo
         if random() < holesPercent :
            lines[0] = lines[0][:i] + Maze.OK + lines[0][i+1:]
            count += 1
      for i in range(1, height - 1) :
         if random() < holesPercent :
            lines[i] = Maze.OK + lines[i][1:]
            count += 1
         if random() < holesPercent :
            lines[i] = lines[i][:-2] + Maze.OK + lines[i][-1]
            count += 1
      for i in range(1, width - 1) : # inutile generare un varco in un angolo
         if random() < holesPercent :
            lines[height - 1] = lines[height - 1][:i] + Maze.OK + lines[height - 1][i+1:]
            count += 1
      if count == 0 : # inserisco un varco
         lines[0] = lines[0][:1] + Maze.OK + lines[0][2:]
      # genero i muri interni
      for i in range(1, height - 1) :
         for j in range(1, width - 1) :
            if lines[i][j] == Maze.OK and random() < wallPercent :
               length = randint(1, wallMaxLength)
               vertical = True if random() < 0.5 else False
               up_or_left = True if random() < 0.5 else False
               # attenzione che non esca dai bordi...
               if vertical :
                  if up_or_left :
                     start = max(1, i - length + 1)
                     end = min(height - 2, start + length)
                  else :
                     end = min(height - 2, i + length - 1)
                     start = max(1, end - length)
                  for k in range(start, end) :
                     lines[k] = lines[k][:j] + Maze.WALL + lines[k][j+1:]
               else :
                  if up_or_left :
                     start = max(1, j - length + 1)
                     end = min(width - 2, start + length)
                  else :
                     end = min(width - 2, j + length - 1)
                     start = max(1, end - length)
                  for k in range(start, end) :
                     lines[i] = lines[i][:k] + Maze.WALL + lines[i][k+1:]
      self._buildAdj()

   def _readFromFile(self, filename) : # metodo privato
      try :
         f = open(filename)
      except FileNotFoundError :
         exit("Il file non esiste")
      self._lines = lines = f.readlines()
      f.close()
      self._width = width = len(lines[0]) - 1 # c'è \n finale
      self._height = height = len(lines)
      for line in lines :
         if len(line) - 1 != width :
            exit("Il labirinto non è rettangolare" + line)
      self._buildAdj()
            
   def _buildAdj(self) : # metodo privato per non ripetere codice
      width = self._width
      height = self._height
      lines = self._lines
      self._adj = dict() # adiacenze
      for i in range(height) :
         line = lines[i]
         for j in range(width) :
            lst = list()
            if i != 0 and lines[i-1][j] == Maze.OK :
               lst.append((i-1, j))
            if i != height-1 and lines[i+1][j] == Maze.OK :
               lst.append((i+1, j))
            if j != 0 and lines[i][j-1] == Maze.OK :
               lst.append((i, j-1))
            if j != width-1 and lines[i][j+1] == Maze.OK :
               lst.append((i, j+1))
            self._adj[(i, j)] = lst            
         
   def __repr__(self) :
      s = ""
      for line in self._lines :
         s += line
      return s

   def help(self) :
      dir = dict()      
      for key in self._adj : # key è una tupla che identifica un corridoio
         dir[key] = Maze.UNKNOWNDIR
      for key in dir : # cerco i corridoi sui margini esterni del labirinto
         if key[0] == 0 :
            dir[key] = "N"
         elif key[1] == self._width - 1 :
            dir[key] = "E"
         elif key[0] == self._height - 1 :
            dir[key] = "S"
         elif key[1] == 0 :
            dir[key] = "W"
      done = False
      while not done :
         done = True
         for key in dir : # per ogni corridoio
            if dir[key] == Maze.UNKNOWNDIR :
               for p in self._adj[key] : # corridoi adiacenti
                  if dir.get(p) != Maze.UNKNOWNDIR :
                     if key[0] < p[0] :
                        dir[key] = "S"
                     elif key[0] > p[0] :
                        dir[key] = "N"
                     elif key[1] < p[1] :
                        dir[key] = "E"
                     else :
                        dir[key] = "W"
                     done = False
                     break
      ss = list()
      for i in range(self._height) :
         s = ""
         for j in range(self._width) :
            if self._lines[i][j] == Maze.WALL :
               s += Maze.WALL
            else : # è un corridoio
               s += dir.get((i, j))
         s += "\n"
         ss.append(s)
      self._helpLines = ss
      print("".join(ss))
      
   def findRoute(self) :
      width = self._width
      height = self._height
      lines = self._lines
      helpLines = self._helpLines
      # genero la posizione di partenza, finché non è un corridoio
      from random import randint
      while True :
         startx = randint(0, width) 
         starty = randint(0, height)
         if helpLines[starty][startx] != Maze.UNKNOWNDIR \
              and helpLines[starty][startx] != Maze.WALL :
            break
      lines[starty] = lines[starty][:startx] + Maze.START + lines[starty][startx + 1:]
      curdir = helpLines[starty][startx]
      (curx, cury) = (startx, starty)
      while True :
         if curdir == "N" :
            if cury == 0 : break
            cury -= 1
         elif curdir == "E" :
            if curx == width - 1 : break
            curx += 1
         elif curdir == "S" :
            if cury == height - 1 : break
            cury += 1
         else : # "W"
            if curx == 0 : break
            curx -= 1
         curdir = helpLines[cury][curx]
         lines[cury] = lines[cury][:curx] + Maze.ROUTE + lines[cury][curx + 1:]            

main()