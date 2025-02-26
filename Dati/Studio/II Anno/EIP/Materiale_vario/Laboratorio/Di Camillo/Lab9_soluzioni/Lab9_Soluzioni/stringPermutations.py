# stringPermutations.py

def main() :
   while True :
      s = input("Inserire la stringa senza caratteri duplicati: ")
      if not hasDuplicates(s) :
         break
   iterList = iterativePermutations(s)
   iterList.sort()
   recurList = recursivePermutations(s)
   recurList.sort()
   if iterList != recurList :
      print("ERRORE")
   else :
      print('Permutazioni della stringa "%s"' % s)
      print(iterList)
      
def iterativePermutations(s) :
   # prerequisito: la stringa non contiene caratteri duplicati
   # altrimenti il risultato non è corretto
   if len(s) == 0 :
      return [] # la stringa vuota non ha permutazioni
   if len(s) == 1 :
      return [s] # la stringa è l'unica permutazione di se stessa
   # quante sono le permutazioni di s ? sono s!
   from math import factorial
   count = factorial(len(s)) 
   # c è la lista dei caratteri presenti nella stringa s
   c = list(s)
   # c è la lista ordinata dei caratteri presenti nella stringa s
   c.sort() 
   # preparo la lista delle permutazioni, che verrà riempita e restituita
   lst = []
   # la prima permutazione è quella con i caratteri ordinati, contenuta in c
   ss = ""
   for x in c :
      ss += x
   lst.append(ss) 
   # genero tutte le altre permutazioni, che sono (count - 1)
   for k in range(count-1) : 
      # procedo a ritroso in c, partendo dal penultimo elemento e
      # cercando il primo elemento che è minore dell'elemento che lo segue
      i = len(s) - 2
      while i >= 0 : 
         if c[i] < c[i + 1] :
            # c[i] è il primo elemento (a partire dalla fine)
            # che è minore dell'elemento che lo segue nella lista c
            #
            # ripartendo a ritroso in c, cerco il primo elemento
            # che è maggiore di c[i]
            j = len(s) - 1
            while c[j] < c[i] :
               j -= 1
            # scambio c[i] con c[j]
            temp = c[i]
            c[i] = c[j]
            c[j] = temp
            # inverto la porzione della lista c compresa tra
            # la posizione i (esclusa) e la fine della lista
            # (se tale porzione è vuota, il ciclo non fa niente)
            i += 1
            j = len(s) - 1
            while i < j :
               temp = c[i]
               c[i] = c[j]
               c[j] = temp
               i += 1
               j -= 1
            # la lista c contiene una nuova permutazione di s,
            # dopodiché interrompo il ciclo interno e genero una
            # nuova permutazione ripetendo la ricerca
            ss = ""
            for x in c :
               ss += x
            lst.append(ss)
            break
         else :
            i -= 1
   return lst

def recursivePermutations(s) :
   # se la stringa contiene caratteri duplicati, la lista restituita
   # conterrà stringhe duplicate, ma saranno comunque presenti
   # tutte le permutazioni della stringa s
   if len(s) == 0 :
      return [] # la stringa vuota non ha permutazioni
   if len(s) == 1 :
      return [s] # la stringa è l'unica permutazione di se stessa
   lst = []
   c = s[0]
   lst2 = recursivePermutations(s[1:]) # tolgo il primo carattere
   # per ogni stringa della lista, aggiungo il primo carattere in
   # tutte le posizioni possibili
   for ss in lst2 :
      for i in range(len(ss)+1) :
         lst.append(ss[:i] + c + ss[i:])
   return lst

def hasDuplicates(s) :
   for i in range(len(s)) :
      for j in range(i+1, len(s)) :
         if s[i] == s[j] :
            return True
   return False

main()