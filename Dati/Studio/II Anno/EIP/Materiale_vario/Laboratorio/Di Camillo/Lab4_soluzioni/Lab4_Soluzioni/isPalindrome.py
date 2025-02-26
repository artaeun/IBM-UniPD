# isPalindrome.py
"""
  Per prima cosa bisogna individuare un algoritmo che risolva il problema:
  la cosa migliore è progettarlo in un caso generale (cioè ben diverso da una
  situazione limite o degenere) e, in un secondo momento, verificare che
  funzioni anche nei casi limite e/o degeneri (se non funzionerà, si gestiranno
  tali situazioni con degli enunciati if da porre prima del caso generale).
  
  Vediamo un possibile algoritmo (il problema si può risolvere in più modi).
  Per ogni carattere della stringa, definiamo come "carattere corrispondente"
  quello che si trova alla medesima distanza dal centro della stringa,
  in direzione opposta.
  Ad esempio, nella stringa "abcde",
  'd' è il carattere corrispondente a 'b',
  mentre 'a' è il carattere corrispondente a 'e'.
  L'algoritmo si può descrivere così:
     per ogni coppia di caratteri corrispondenti
        se i due caratteri sono diversi tra loro
           allora la stringa non è un palindromo
              (per confrontare due caratteri, costruiamo due sottostringhe di lunghezza uno)
     terminata la scansione delle coppie, se nessuna coppia era costituita da
     caratteri diversi, allora la stringa è un palindromo

  Per analizzare tutte le coppie, la cosa migliore è procedere ordinatamente,
  ad esempio iniziando dalla coppia più "esterna" (cioè più lontana dal
  centro della stringa), che è costituita dal primo e dall'ultimo carattere,
  per poi proseguire con la seconda coppia, costituita dal secondo e dal penultimo carattere.
  Le prime due stringhe da confrontare sono, quindi
  (chiamata s la stringa da verificare):
     left = s[0]         # primo carattere
     right = s[len(s)-1] # ultimo carattere, si può anche scrivere s[-1]
  La seconda coppia di stringhe da confrontare è, quindi:
     left = s[1]         # secondo carattere
     right = s[len(s)-2] # penultimo carattere, si può anche scrivere s[-2]
     E così via...
  Per compiere azioni ripetitive, bisogna programmare un ciclo.
  Di che tipo? Dobbiamo analizzare ciascun singolo carattere della stringa s
  (nella forma di sottostringa di lunghezza unitaria), insieme al suo
  carattere corrispondente. Sappiamo, quindi, quante sono le iterazioni
  necessarie: len(s). Scriviamo un ciclo a contatore:
  
     i = 0
     while i < len(s) :
        ...
        i += 1

  Cosa mettiamo nel corpo? Per distinguere una iterazione dall'altra,
  cioè per eseguire le stesse operazioni su dati diversi (nel nostro caso,
  su una diversa coppia di caratteri corrispondenti), possiamo usare la
  variabile i, che, iterazione dopo iterazione, assumerà
  i valori: 0, 1, 2, ..., len(s)-1 (che sara' l'ultimo),
  che sono proprio gli indici di uno dei caratteri che costituisce
  la coppia da esaminare!

     i = 0
     while i < len(s) :
        left = s[i]
        right = s[len(s)-i-1]
        if left != right :
           ... # trovata una coppia di caratteri corrispondenti e diversi tra loro
        else :
           ... # trovata una coppia di caratteri corrispondenti e uguali tra loro
        i += 1
        
  In realtà non serve controllare tutte queste coppie... perché quando
  l'indice è arrivato a metà della stringa...

  Finora ci siamo disinteressati dei casi limite e degeneri... vedremo.
  
"""
s = input("Inserire la stringa da verificare: ")
"""
  verificare con attenzione che il valore finale di i nel ciclo
  seguente sia quello corretto sia quando la lunghezza della stringa
  è pari, sia quando è dispari; porre particolare attenzione a
  questo problema anche nel collaudo del programma
"""
isPalindrome = True # così la stringa vuota è un palindromo...
i = 0
while i < len(s) // 2 :
   left = s[i]
   right = s[len(s)-i-1]
   if left != right :
      isPalindrome = False
   i += 1
if isPalindrome :
   print(s, "è un palindromo");
else :
   print(s, "non è un palindromo");