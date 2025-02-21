# triangle.py (module)

from math import isclose

class Point :

   def __init__(self, x, y) :
      self._x = x
      self._y = y
      
   def x(self) :
      return self._x
      
   def y(self) :
      return self._y
      
   def xy(self) :
      return (self._x, self._y)
      
   def delta(p1, p2) :
      return ((p1._x - p2._x)**2 + (p1._y - p2._y)**2)**(1/2)

class Triangle : 
   # dato che i singoli punti che definiscono il triangolo non vengono
   # utilizzati dai metodi, che invece usano le lunghezze dei lati, è
   # più comodo usare quelle come variabili di esemplare; siccome, poi,
   # alcuni metodi hanno bisogno di sapere quale sia il lato più lungo,
   # memorizziamo le lunghezze dei lati in ordine decrescente in una
   # tupla (non serve una lista, perché nessun metodo li modifica)
   def __init__(self, p1, p2, p3) :
      sides = (Point.delta(p1,p2), Point.delta(p2,p3), Point.delta(p1,p3))
      maxSide = max(sides)
      minSide = min(sides)
      middleSide = sum(sides) - minSide - maxSide
      self._sides = (maxSide, middleSide, minSide)
      if maxSide >= middleSide + minSide :
         raise ValueError("I punti non definiscono un triangolo")
       
   def area(self) : # uso la formula di Erone
      (d1, d2, d3) = self._sides
      p = (d1 + d2 + d3) / 2
      return (p * (p - d1) * (p - d2) * (p - d3))**(1/2)
      
   def height(self) : # l'altezza relativa al lato maggiore
      return 2 * self.area() / self._sides[0]
      
   def isScalene(self) :
      (d1, d2, d3) = self._sides
      return not isclose(d1, d2) and not isclose(d2, d3) and not isclose(d1, d3)
      
   def isIsosceles(self) :
      (d1, d2, d3) = self._sides
      return isclose(d1, d2) or isclose(d2, d3) or isclose(d1, d3)
      
   def isEquilateral(self) :
      (d1, d2, d3) = self._sides
      # osservare che, ovviamente, la relazione indotta da isclose NON è
      # transitiva... quindi devo controllare le tre coppie di lati
      # infatti, ad esempio, d1 potrebbe essere prossimo a d2 e d2
      # potrebbe essere prossimo a d3, ma la differenza tra d1 e d3
      # potrebbe essere eccessiva
      return isclose(d1, d2) and isclose(d2, d3) and isclose(d1, d3)
      
   def isRight(self) :
      (d1, d2, d3) = self._sides
      # verifico se la formula pitagorica è rispettata, l'ipotenusa
      # è ovviamente il lato più lungo, cioè d1
      return isclose(d1*d1, d2*d2 + d3*d3)òòòòòòòòòòòòòòòòòò

if __name__ == "__main__" :
   # codice di collaudo
   t = Triangle(Point(0, 0), Point(1, 1), Point(0, 1))
   print(t.area())
   print(t.isRight()) # osservare che senza l'uso di isclose sarebbe False
   print(t.isScalene())
   print(t.isEquilateral())
   print(t.isIsosceles())
   # aggiungere molte altre prove...