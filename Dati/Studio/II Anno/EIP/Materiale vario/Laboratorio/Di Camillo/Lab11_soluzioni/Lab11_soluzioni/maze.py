# maze.py

from sys import exit

def main() :
   m = Maze("maze.txt")
   print(m)
   m.help()

class Maze :

   OK = " "
   WALL = "*"
   
   def __init__(self, filename) :
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
      
   def _reprStep(self, dir) : # metodo privato usato da help
      s = ""
      for i in range(self._height) :
         for j in range(self._width) :
            if self._lines[i][j] == Maze.WALL :
               s += Maze.WALL
            else : # è un corridoio
               s += dir.get((i, j))
         s += "\n"
      return s

   def help(self) :
      dir = dict()      
      for key in self._adj : # key è una tupla che identifica un corridoio
         dir[key] = "?"
      for key in dir : # cerco i corridoi sui margini esterni del labirinto
         if key[0] == 0 :
            dir[key] = "N"
         elif key[1] == self._width - 1 :
            dir[key] = "E"
         elif key[0] == self._height - 1 :
            dir[key] = "S"
         elif key[1] == 0 :
            dir[key] = "W"
      print(self._reprStep(dir))
      done = False
      while not done :
         done = True
         for key in dir : # per ogni corridoio
            if dir[key] == "?" :
               for p in self._adj[key] : # corridoi adiacenti
                  if dir.get(p) != "?" :
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
         print(self._reprStep(dir))               

main()