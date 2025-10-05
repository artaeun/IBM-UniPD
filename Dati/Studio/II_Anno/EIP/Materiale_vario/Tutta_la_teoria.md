# Indice
- [1. Variabili e operazioni](#1-variabili-e-operazioni)
  - [*Variabili*](#variabili)
    - [Assegnazione variabili](#assegnazione-variabili)
    - [Conversione di tipo](#conversione-di-tipo)
    - [Altre funzioni per le variabili](#altre-funzioni-per-le-variabili)
  - [*Operazioni*](#operazioni)
    - [Operatori aritmetici](#operatori-aritmetici)
    - [Algoritmo confronto tra numeri di tipo float](#algoritmo-confronto-tra-numeri-di-tipo-float)
    - [Modulo ***math*** di Python](#modulo-math-di-python)
  - [*Input/Output*](#inputoutput)
- [2. Decisioni, eccezioni, exit](#2-decisioni-eccezioni-exit)
  - [Tabulazioni](#tabulazioni)
  - [*Operatori relazionali*](#operatori-relazionali)
  - [*Operatori logici*](#operatori-logici)
  - [*Condizionale IF*](#condizionale-if)
    - [Assegnazione condizionale](#assegnazione-condizionale)
    - [Assegnazione condizionale 2](#assegnazione-condizionale-2)
    - [Correzione usando _try/except_:](#correzione-usando-tryexcept)
  - [*exit()*](#exit)
- [3. Condizionali](#3-condizionali)
  - [*Ciclo WHILE*](#ciclo-while)
    - [Forma base](#forma-base)
  - [*Ciclo FOR*](#ciclo-for)
    - [Forma base:](#forma-base-1)
    - [Un'altra forma:](#unaltra-forma)
    - [La funzione _range()_:](#la-funzione-range)
    - [Altro modo per usare _range()_:](#altro-modo-per-usare-range)
  - [*Funzioni per numeri casuali*](#funzioni-per-numeri-casuali)
  - [*Metodo Monte Carlo*](#metodo-monte-carlo)
  - [*IS / IS NOT*](#is--is-not)
    - [Uso delle funzioni:](#uso-delle-funzioni)
- [4. Stringhe](#4-stringhe)
	- [Slicing](#slicing)
	- [Operatore logico IN](#operatore-logico-in)
	- [Confronto tra stringhe](#confronto-tra-stringhe)
	- [Metodi per le stringhe](#metodi-per-le-stringhe)
	- [Funzione *.lower() e .upper()*](#funzione-lower-e-upper)
	- [Funzione *.find()*](#funzione-find)
	- [Funzione *.replace()*](#funzione-replace)
	- [Funzioni *.lstrip()* / *.rstrip()* / *.strip()*](#funzioni-lstrip--rstrip--strip)
	- [Funzioni *.startswith()*](#funzioni-startswith)
    - [Codifica Unicode](#codifica-unicode)
    - [Caratteri speciali](#caratteri-speciali)
      - [***Uso più esteso dei caratteri speciali***](#uso-più-esteso-dei-caratteri-speciali)
- [5. File](#5-file)
  - [*Gestione file*](#gestione-file)
    - [Aprire un file in lettura](#aprire-un-file-in-lettura)
    - [Aprire un file in scrittura](#aprire-un-file-in-scrittura)
    - [Scrivere su file](#scrivere-su-file)
    - [Chiudere un file](#chiudere-un-file)
  - [*Leggere l'intero file*](#leggere-lintero-file)
    - [Leggere l'intero file assegnandolo a un'unica stringa](#leggere-lintero-file-assegnandolo-a-ununica-stringa)
    - [Leggere il file riga per riga](#leggere-il-file-riga-per-riga)
    - [Leggere un file riga per riga con il ciclo *for*](#leggere-un-file-riga-per-riga-con-il-ciclo-for)
  - [*Cercare all'interno di un file*](#cercare-allinterno-di-un-file)
    - [Metodo con il ciclo for](#metodo-con-il-ciclo-for)
    - [Aprire file da "nome file" dato dall'utente](#aprire-file-da-nome-file-dato-dallutente)
      - [Gestire eccezioni relative al nome dei file](#gestire-eccezioni-relative-al-nome-dei-file)
    - [Leggere parole elaborando da file](#leggere-parole-elaborando-da-file)
- [6. Espressioni regolari](#6-espressioni-regolari)
  - [Cosa sono le espressioni regolari](#cosa-sono-le-espressioni-regolari)
    - [find()](#find)
    - [re.search()](#research)
    - [Greedy Matching](#greedy-matching)
    - [Non-Greedy Matching](#non-greedy-matching)
- [7. Liste](#7-liste)
  - [_Liste_](#liste)
    - [Definizione](#definizione)
    - [Slicing](#slicing-1)
      - [Rispetto alle stringhe](#rispetto-alle-stringhe)
    - [Lunghezza lista](#lunghezza-lista)
    - [La funzione .range()](#la-funzione-range-1)
    - [Riferimento alla lista](#riferimento-alla-lista)
    - [Copiare una lista con .list()](#copiare-una-lista-con-list)
      - [Casi particolari:](#casi-particolari)
    - [Concatenazione liste:](#concatenazione-liste)
  - [_Metodi per liste_](#metodi-per-liste)
    - [Funzioni che hanno argomenti di tipo _list_:](#funzioni-che-hanno-argomenti-di-tipo-list)
    - [Aggiungere elementi in una lista](#aggiungere-elementi-in-una-lista)
    - [Inserire elementi in una lista](#inserire-elementi-in-una-lista)
    - [Cercare elementi in una lista](#cercare-elementi-in-una-lista)
    - [Rimuovere/Eliminare elementi in una lista](#rimuovereeliminare-elementi-in-una-lista)
    - [Ordinare elementi in una lista](#ordinare-elementi-in-una-lista)
      - [Un modo per ordinare elementi da una lista è utilizzare il metodo _sort_.](#un-modo-per-ordinare-elementi-da-una-lista-è-utilizzare-il-metodo-sort)
    - [Ordinare elementi in una lista](#ordinare-elementi-in-una-lista-1)
  - [_Tabelle e matrici_](#tabelle-e-matrici)
  - [_Appendere argomenti/file al codice sorgente_](#appendere-argomentifile-al-codice-sorgente)
  - [_Tuple_](#tuple)
    - [Funzioni che si possono usare con le tuple: _count_, _index_.](#funzioni-che-si-possono-usare-con-le-tuple-count-index)
    - [Assegnazione](#assegnazione)
- [8. Grafica](#8-grafica)
  - [Cosa usare per la grafica](#cosa-usare-per-la-grafica)
  - [ezgraphics](#ezgraphics)
    - [Come usarlo](#come-usarlo)
    - [RGB](#rgb)
    - [Colore riempimento](#colore-riempimento)
    - [Outline](#outline)
    - [Testo](#testo)
  - [tkinter](#tkinter)
    - [Come usarlo](#come-usarlo-1)
    - [RGB, fill, outline, testo](#rgb-fill-outline-testo)
    - [Immagini](#immagini)
- [9. Insiemi e dizionari](#9-insiemi-e-dizionari)
  - [9.1 *Insiemi*](#81-insiemi)
    - [Come crearli](#come-crearli)
    - [Lunghezza](#lunghezza)
    - [Aggiungere elementi](#aggiungere-elementi)
    - [Eliminare elementi](#eliminare-elementi)
      - [.discard()](#discard)
      - [.remove()](#remove)
      - [.clear()](#clear)
    - [Sottoinsiemi](#sottoinsiemi)
      - [Uguaglianza](#uguaglianza)
      - [Unione di due insiemi](#unione-di-due-insiemi)
      - [Intersezione e differenza](#intersezione-e-differenza)
    - [Il programma spellcheck.py](#il-programma-spellcheckpy)
  - [9.2 *Dizionari*](#82-dizionari)
    - [*Dizionario*](#dizionario)
    - [_Come crearli_](#come-crearli-1)
    - [_Aggiungere elementi_](#aggiungere-elementi-1)
    - [_Usare i valori di un elemento_](#usare-i-valori-di-un-elemento)
    - [_Eliminare coppie_](#eliminare-coppie)
    - [_Iterare/Scandire gli elementi di un dizionario_](#iterarescandire-gli-elementi-di-un-dizionario)
    - [_Verificare presenza di chiave nel dizionario_](#verificare-presenza-di-chiave-nel-dizionario)
    - [_Verificare presenza di chiave nel dizionario_](#verificare-presenza-di-chiave-nel-dizionario-1)
    - [_Metodo __get___](#metodo-get)
    - [_Due variabili di iterazione_](#due-variabili-di-iterazione)
    - [_Recuperare la lista di chiavi e valori di un dizionario_](#recuperare-la-lista-di-chiavi-e-valori-di-un-dizionario)
    - [_Tuple e operatori di confronto_](#tuple-e-operatori-di-confronto)
    - [_Ordinare un dizionario rispetto a __key___](#ordinare-un-dizionario-rispetto-a-key)
    - [_Ordinare un dizionario rispetto a __value___](#ordinare-un-dizionario-rispetto-a-value)
    - [_Copiare i dizionari_](#copiare-i-dizionari)
- [10. Funzioni](#10-funzioni)
  - [_Definizione e invocazione_](#definizione-e-invocazione)
  - [_Definire più parametri_](#definire-più-parametri)
  - [_Passaggio di parametri_](#passaggio-di-parametri)
  - [_Utilizzo di liste come parametri_](#utilizzo-di-liste-come-parametri)
  - [_Utilizzo di tuple come parametri_](#utilizzo-di-tuple-come-parametri)
  - [_Visibilità/Scope delle variabili_](#visibilitàscope-delle-variabili)
    - [_Variabili globali_](#variabili-globali)
  - [_Return_](#return)
  - [_Consigli per scrivere codice sfruttando le funzioni_](#consigli-per-scrivere-codice-sfruttando-le-funzioni)
  - [_Moduli_](#moduli)
  - [_Documentazione automatica della propria funzione_](#documentazione-automatica-della-propria-funzione)
  - [*Cos'è la ricorsione?*](#cosè-la-ricorsione)
    - [_Esempio ricorsione: Fibonacci_](#esempio-ricorsione-sequenza-di-fibonacci)
  - [_Itterativo o Ricorsivo?_](#itterativo-o-ricorsivo)
  - [_Mappatura_](#mappatura)
  - [_Filtraggio_](#filtraggio)
  - [_Riduzione_](#riduzione)
- [11. Classi](#11-classi)
  - [_Cosa sono le classi_](#cosa-sono-le-classi)
  - [_Metodi_](#metodi)
  - [_Come definire una classe e i suoi metodi_](#come-definire-una-classe-e-i-suoi-metodi)
  - [_Incapsulamento_](#incapsulamento)
  - [_Costruttori_](#costruttori)
    - [*Argomenti di Default*](#argomenti-di-default)
  - [_Collaudare una classe_](#collaudare-una-classe)
  - [_Variabile di classe_](#variabile-di-classe)
  - [_Tenere traccia degli oggetti_](#tenere-traccia-degli-oggetti)
  - [_Schemi ricorrenti_](#schemi-ricorrenti)
  - [_Vita di un oggetto_](#vita-di-un-oggetto)
  - [_Aliasing e riferimento self_](#aliasing-e-riferimento-self)
  - [_Copiare un oggetto_](#copiare-un-oggetto)
- [12. Debugging](#12-debugging)
  - [_Uso di Pdb_](#uso-di-pdb)
  - [_Commandi Pdb_](#commandi-pdb)
- [13. Eccezioni](#13-eccezioni)
  - [_Cosa sono?_](#cosa-sono)
    - [Eccezioni specifiche e generiche](#eccezioni-specifiche-e-generiche)
  - [_finally_](#finally)
  - [_raise_](#raise)
- [14. Ereditarietà](#14-ereditarietà)
  - [*Cos'è*](#cosè)
  - [*Principio di sostituzione (substitution principle)*](#principio-di-sostituzione-substitution-principle)
  - [14.1 *Sottoclassi ed ereditarietà*](#141-sottoclassi-ed-ereditarietà)
  - [14.2 Superclasse ***object***](#142-superclasse-object)
  - [14.3 Costruttori](#143-costruttori)
  - [14.4 Sovrascrivere un metodo (override)](#144-sovrascrivere-un-metodo-override)
  - [14.5 Polimorfismo_](#145-polimorfismo)
  - [_Classi e metodi astratti_](#classi-e-metodi-astratti)
- [15. Algoritmi](#15-algoritmi)
  - [Ricerca binaria/dicotomica/bisezione](#ricerca-binariadicotomicabisezione)
    - [_Algoritmo iterativo_](#algoritmo-iterativo)
    - [_Algoritmo ricorsivo_](#algoritmo-ricorsivo)
- [16. Analisi delle prestazioni e sorting](#16-analisi-delle-prestazioni-e-sorting)
  - [Analisi delle prestazioni degli algoritmi](#analisi-delle-prestazioni-degli-algoritmi)
    - [Andamento asintotico delle prestazioni](#andamento-asintotico-delle-prestazioni)
    - [Notazione O-grande](#notazione-o-grande)
    - [Notazione Omega](#notazione-omega)
    - [Notazione Theta](#notazione-theta)
  - [Ordinamento per selezione (Selection Sort)](#ordinamento-per-selezione-selection-sort)
    - [Prestazioni dell’algoritmo](#prestazioni-dell'-algoritmo)
  - [Ordinamento per inserimento (Insertion Sort)](#ordinamento-per-inserimento-insertion-sort)
    - [Prestazioni dell’algoritmo](#prestazioni-dell'-algoritmo)
  - [Ordinamento per fusione (Merge Sort)](#ordinamento-per-fusione-merge-sort)
    - [Prestazioni dell’algoritmo](#prestazioni-dell'-algoritmo)
    - [Merge Sort iterativo](#merge-sort-iterativo)
    - [Confronto di algoritmi](#confronto-di-algoritmi)
  - [Quick Sort](#quick-sort)
    - [Prestazioni dell’algoritmo](#prestazioni-quick-sort)
  - [Ricerca di un elemento](#ricerca-di-un-elemento)
- [17. Strutture dati](#17-strutture-dati)
  - [Referential array](#referential-array)
    - [Puntualizzazione rispetto ad aliasing, shallow copy e deep copy](#puntualizzazione-rispetto-ad-aliasing-shallow-copy-e-deep-copy)
    - [Array compatti](#array-compatti)
    - [Array dinamici](#array-dinamici)
  - [Inserimenti e rimozioni in un array](#inserimenti-e-rimozioni-in-un-array)
  	- [Rimozione di un elemento](#rimozione-di-un-elemento)
	- [Inserimento di un elemento](#inserimento-di-un-elemento)
- [18. Metodi di istanza e di classe](#18-metodi-di-istanza-e-di-classe)
- [19. Pile e code](#19-pile-e-code)
   - [Pila (stack)](#pila-stack)
     - [Prestazioni](#prestazioni-pila)
   - [Coda (queue)](#coda-queue)
     - [Code ad implementazione circolare](#code-ad-implementazione-circolare)
- [20. Linked lists](#20-linked-lists)
   - [Metodi di classe](#metodi-di-classe-linked-lists)
   - [Pila realizzata con una catena](#pila-realizzata-con-una-catena)
   - [Coda realizzata con una catena](#coda-realizzata-con-una-catena)
   - [Coda doppiamente concatenata](#coda-doppiamente-concatenata)
   - [Catena o Array?](#catena-o-array)


# 1. Variabili e operazioni
## *Variabili*
Nomi permessi delle variabili → nomi che iniziano con una lettera o un underscore. Caratteri succesivi devono essere cifre, lettere o underscores. È case sensitive

### Assegnazione variabili
```python
x=12 #intero
y=1.2 #float
z="Ciao" #string
```

### Conversione di tipo
```python
y=int(x) #converte x in un intero e salva in y
y=float(x) #converte x in un float, variabile a virgola mobile
y=str(x) #converte x in una stringa e salva in y
```

### Altre funzioni per le variabili
```python
#===Tipo dato===
type(x) #ci ritorna il tipo della variabile x

#===Lunghezza stringa===
length=len("World!") #length ha valore 6

#===Concatenazione===
firstName="Harry"
lastName="Potter"
fullName = firstName + " " +lastName 
# fullName="Harry Potter"

#===Sottostringhe===
print(firstName[0])
#ritorna "H"
print(firstName[len(firstName)-1])
#ritorna "y"
print(firstName[0,3])
#ritorna "Har"
print(firstName[:3])
#ritorna "Har"
print(firstName[3:])
#ritorna "ry"
print(firstName[:])
#ritorna "Harry"

#===Ripetizione stringa===
stringa="x"
print(x*3)
#ritorna "xxx"
``` 

___

## *Operazioni*

### Operatori aritmetici
```python
z = x + y  #addizione
z = x - y  #sottrazione
z = x * y  #moltiplicazione
z = x / y  #divisione
z = x ** y #elevamento a potenza y
z = x // y #divisione intera (risultato è l'intero)
z = x % y  #resti divisione intera (modulo)
``` 
### Algoritmo confronto tra numeri di tipo float

```python
from math import sqrt
EPSILON = 1E-14
r = sqrt(2.0)
if abs(r*r - 2.0)<EPSILON : print("sqrt(2.0) squared is approximately 2.0")
```
### Modulo ***math*** di Python

Basta importarlo per usare le funzioni varie offerte.

```python
from math import * #o per ottimizzare si può fare
from math import sqrt

y=sqrt(x)     #radice quadrata
y=trunc(x)    #tronca il valore in intero
y=cos(x)      #coseno di x in radianti
y=sin(x)      #sinx in rad
y=tan(x)      #tan di x in rad
y=exp(x)      #e^x
y=degrees(x)  #x da rad in °
y=radians(x)  #x da ° in rad
y=log(x)      #log x in base e
y=log(x,base) #log x in base indicata

#in alternativa:
import math

math.log2(8)
```

Per controllare le funzioni disponibili basta fare nel IDLE:

```python
import math
dir(math)
```
## *Input/Output*

```python
name = input("Chi sei?") #stampa "Chi sei", e riceve input
#input è SEMPRE una string
print(name) #stampa il nome ricevuto in input
```


# 2. Decisioni, eccezioni, exit

## Tabulazioni
Python richiede come tabulazione 4 spazi. Più o di meno di 4 e darà errore.

## *Operatori relazionali*

|Operatori|Funzione|
|:---:|---|
|<|minore di|
|>|maggiore|
|<=|minore o uguale|
|>=|maggiore o uguale|
|!=|diverso|
|==|uguale|

L'operatore ***=*** viene usato solo per assegnare, non per confrontare.

## *Operatori logici*

|Operatori|Funzione|
|:---:|---|
|AND|TRUE se e solo se sia A che B sono vere|
|OR|TRUE se A o B sono vere|
|NOT|inverte il valore della variabile boolean|
___
## *Condizionale IF*
```python
if x<3:
  print("something")
elif x=3:
  #do something else
else:
  #se nessuno dei n condizionali viene verificato, fai questa cosa
```
### Assegnazione condizionale
```python
variabile = 2 if x>0 else 3
```
### Assegnazione condizionale 2
```python
actualFloor= floor-1 if floor > 3 else floor

#che È equivalente a:
if floor>13:
  actualFloor=floor-1
elif floor=13:
	dp=3
else:
  actualFloor=floor

___
## *Eccezioni - Try/Except*

### Codice che da eccezione:
```python
astr="Una stringa qualsiasi"
istr=int(astr)
```
### Correzione usando _try/except_:

```python
try: #prova a fare questo
	istr=int(astr)
except: #se ti da eccezione, errori, ecc, esegui questo
	istr=-1
```
Cerca sempre di minimizzare il codice all'interno del try per ottimizzare il codice.

___
## *exit()*

```python
from sys import exit

exit()
#fa terminare immediatamente il programma. 
#È definita nel modulo sys della libreria standard'

exit("Error, you did some stupid shit so i exited the program.") 
#termina l'esecuzione del programma con un messaggio.'
```

# 3. Condizionali

## *Ciclo WHILE*

### Forma base
```python
while booleanConditionTrue:
	#do whatever
```

Il ciclo finisce quando booleancondition diventa falsa. Altrimenti si finisce in un loop.
```python
while True:
	line=input()
	if line[0]=='#'
		continue #continua
	if line=='donÈ
		break #rompe il ciclo while
	print (line)
print('DonÈ)
#questo codice stamperà mano a mano ogni riga scritta,
#e si fermera' solo quando gli inviamo 'donÈ
```
___
## *Ciclo FOR*

### Forma base:
```python
for i in [5,4,3,2,1]:
	print(i) #prints: 5,4,3,2,1,Blastoff!
print('Blastoff!') 
```
### Un'altra forma:
```python
friends = ['Joseph', 'Glenn', 'Sally']
for friends in friends:
	print('Happy New Year', friends)#Happy New Year: Joseph, ecc.
print('Done!')
```
### La funzione _range()_:
```python
for i in range(1,10):
	print(i)
```
che equivale a:
```python
i=1
while i<10:
	print(i)
	i = i + 1
```

La funzione _range(n,m)_ genera numeri interi nel range proposto tra _n_ ed _m_. Es.: range(1,4) => 1,2,3. Utile solo con il ciclo _for_.

### Altro modo per usare _range()_:

```python
for i in range(1,5):
	#do something
```
equivalente a:
```python
for i in range(5):
	#do something
```

Altro esempio con _range_ ma usando un valore incrementale:
```python
for i in range(1,11,2):
	#do whatever
  
#il terzo valore è l'incremento del range. Es:
# 1+2,3+2, ecc.
```
___

## *Funzioni per numeri casuali*
```python
from random import *

random() #ritorna un nr. casuale tra 0 e 1
randint(a,b) #ritorna un nr. casuale int tra a e b
```

## *Metodo Monte Carlo*

Trova soluzioni approssimate a problemi i cui risultati non possono essere precisi. Per esempio, per calcolare PiGreco.

Metodo:
1. simuli il lancio di una frecettetta all'interno di un quadrato circoscritto a un cerchio di raggio 1 e centro (0,0)
2. basta generare valori casuali tra -1 e 1 per x e y
2.1 se il punto generato è dentro al cerchio, allora il bersaglio è "colpito": questo se x^2 + y^2 <=1
3. dato che i lanci sono casuali, ci aspettiamo che i hits/tries sia circa uguale al rapproto tra le aree del cerchio e del quadrato, cioÈ pi/4
4. la stima del nostro valore di pi È uguale a: 4*hits/tries
___

## *IS / IS NOT*

### Uso delle funzioni:

Fai qualcosa se la variabile non ha mai ricevuto valore:
```python
if smallest is None: #do something
```

Fai qualcosa se la variabile ha un qualsiasi valore. 
```python
if smallest is not None: #do something
```
Non puoi usare _non==None_ o _!=None_ per usare questo valore speciale. 



# 4. Stringhe

In Python 3 tutte le stringhe sono una sequenza di caratteri Unicode (non è necessario nemmeno specificare che è in Ascii Unicode).

### Slicing

Il tagliare di una porzione di stringa:

```python
>>> s = 'Monty Python'
>>> print(s[:2])
Mo
>>> print(s[8:])
thon
>>> print(s[:])
Monty Python
```

### Operatore logico IN

L’operatore in può essere usato per capire se una stringa è contenuta in un’altra. *"in"* è un operatore logico che restituisce True o False e quindi può essere usato in un enunciato *if*.

```python
>>> fruit = 'banana'
>>> 'n' in fruit
True
>>> 'm' in fruit
False
>>> 'nan' in fruit
True
>>> if 'a' in fruit :
... print('Found it!')
Found it!
>>>
```

I tre puntini sono necessari in modalità interattiva da shell per andare a capo con l’istruzione.

### Confronto tra stringhe

Gli operatori relazionali confrontano le stringhe secondo l’ordinamento  
lessicografico. In Python:

- tutte le lettere maiuscole precedono tutte le lettere minuscole (ad esempio,  
    “Z” precede “a”);
- il carattere “spazio” precede tutti i caratteri visualizzabili;
- i numeri precedono le lettere;

```python
if word == 'banana':
print('All right, bananas.')
if word < 'banana':
print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
print('Your word,' + word + ', comes after banana.')
else:
print('All right, bananas.')
```

Per confrontare due stringhe, si inizia confrontando la prima lettera di ciascuna stringa, poi si procede confrontando la seconda lettera, e così via, finché una delle stringhe termina oppure si trova una coppia di lettere tra loro diverse.

### Metodi per le stringhe

La libreria standard *String* contiene metodi che possono essere evocati senza importare nulla.

```python
str.capitalize()
str.center(width[, fillchar])
str.endswith(suffix[, start[, end]])
str.find(sub[, start[, end]])
str.lstrip([chars])
str.replace(old, new[, count])
str.lower()
str.rstrip([chars])
str.strip([chars])
str.upper()
```

### Funzione *.lower() e .upper()*

```python
>>> greet = 'Hello Bob'
>>> zap = greet.lower()
>>> print(zap)
hello bob
>>> print(greet)
Hello Bob
>>> print('Hi TherÈ.lower())
hi there
>>> print('Hi TherÈ.upper())
HI THERE
>>>
```

### Funzione *.find()*

Il metodo *find(sub\[, start\[, end\]\])* cerca la prima occorrenza dell’argomento *sub*. Se la trova restituisce l’indice corrispondente, altrimenti restituisce -1.

```python
>>> fruit = 'banana'
>>> pos = fruit.find('na')
>>> print(pos)
2
>>> aa = fruit.find('z')
>>>
```

In genere, prima di usare *find()* si fa una conversione in minuscolo o maiuscolo così da cercare indipendentemente dal fatto che i caratteri siano in minuscolo o maiuscolo.

### Funzione *.replace()*

La funzione *replace()* funziona come “search and replace” in Word: trova e sostiuisce tutte le occorrenze.

```python
>>> greet = 'Hello Bob'
>>> nstr = greet.replace('Bob','JanÈ)
>>> print(nstr)
Hello Jane
>>> nstr = greet.replace('o','X')
>>> print(nstr)
HellX BXb
```

### Funzioni *.lstrip()* / *.rstrip()* / *.strip()*

Alle volte è utile rimuovere spazi bianchi all’inizio o alla fine di una stringa.

*.lstrip()* / *.rstrip()* rimuovono gli spazi a sn e a dx rispettivamente.

*.strip()* rimuove sia a sn che a dx.

```python
>>> greet = ' Hello Bob '
>>> greet.lstrip()
'Hello Bob '
>>> greet.rstrip()
' Hello Bob'
>>> greet.strip()
'Hello Bob'
>>>
```

### Funzioni *.startswith()*

```python
>>> line = 'Please have a nice day'
>>> line.startswith('PleasÈ)
True
>>> line.startswith('p')
False
```

## Codifica Unicode

Un carattere viene memorizzato all’interno dei calcolatori come se fosse un numero intero e lo specifico valore usato per ciascun carattere dipende da un insieme standard di codici (ASCII).

```python
print(“The letter H has a code of”, ord(“H”))
# The letter H has a code of 72
print(“Code 97 represents the character”, chr(97))
# Code 97 represents the character a
```

## Caratteri speciali

- *Escape* \- permette di inserire caratteri speciali come il *"* senza rompere la stringa.

```python
print("He said \"Hello\"")
print("C:\\Temp\\File.txt") 
#nel caso del carattere /, si usa il doppio Escape
```

- *NewLine* \- è una sequenza di escape che stampa il carattere *newline*.

```python
print(“*\n**\n***”)
# Stampa:
# *
# **
# ***
```

- *Operatore di formato* \- si usa se si vuole controllare il formato di visualizzazione di un'elaborazione.

```python
>>>price = 1.22354
>>>print(“%.2f” % price)#due cifre dopo il punto decimale
1.22
>>>print(“%10.3f” % price)#il 10 indica l'ampiezza di campo
1.224
```

L'ampiezza di campo non è solo specifica ai numeri dopo la virgola ma anche quelli prima. L'impostazone “%2.2f” per esempio, per il numero *340.22523* sarà quindi *40.22*.

La lettera *f* è per i numeri a virgola mobile. Le impostazioni sono le seguenti:

| Indicatore | Funzione |
| --- | --- |
| "%d" | interi |
| "%f" | a virgola mobile |
| "%s" | stringhe |

### ***Uso più esteso dei caratteri speciali***

Con un’unica stringa avente indicatori di formato si può imporre il formato desiderato a più valori, che vanno, però, racchiusi da una coppia di parentesi tonde e separati da virgole:

```python
total = 17.29214
quantity = 24
print(“Quantity: %d Total: %10.2f” % (quantity, total))
#Stampa:
#Quantity: 24 Totale:     17.29
```

Da notare che ci sono dieci spazi tra l'ultimo spazio dopo "Totale:" e il 9 di *17.29*.

Quando viene specificata l’ampiezza di un campo, i valori vengono allineati a destra all’interno del numero di colonne indicato: mentre questa disposizione è solitamente quella desiderata nel caso di valori numerici visualizzati in una tabella, spesso non è adeguata per le stringhe.  
Per specificare un allineamento a sinistra, basta aggiungere un segno meno prima dell’ampiezza del campo relativo alle stringhe:

```python
print(“%–10s %10d” % (title1, 24))
# Quantity: 24
print(“%–10s %10.2f” % (title2, 17.29))
# Price: 17.29
```



# 5. File

Un file di testo può essere pensato come una sequenza di righe.

## *Gestione file*
### Aprire un file in lettura
```python
handle = open(“input.txt”, “r”)
```
* L'enunciato apre il file per la lettura (come indicato dall’argomento “r”, che sta per read, cioè “leggere”) e restituisce un oggetto di tipo file (file object) che è stato associato al file input.txt.

* Quando un file viene aperto, un apposito contrassegno o cursore (marker) viene posizionato all’inizio del file stesso in corrispondenza alla prima riga.

* Quando si apre un file in lettura, il file deve esistere, altrimenti si verifica un errore.

### Aprire un file in scrittura
```python
file_modifica = open(“output.txt”, “w”)
```
Il secondo argomento deve essere la stringa “w” (che sta per write, cioè “scrivere”).
Se il file output.txt non esiste, viene creato vuoto. Se invece esiste già, viene svuotato completamente prima che vi vengano scritti i nuovi dati. Questo può sovrascrivere completamente file, quindi fare particolare attenzione

### Scrivere su file

```python
file_modifica = open(“output.txt”, “w”)
file_modifica.write(“Hello, World!\n”)
```

* Quando si scrive testo in un file, bisogna scrivere esplicitamente il carattere \n per iniziare una nuova riga.
* Il metodo write riceve come argomento una sola stringa e la scrive immediatamente nel file, aggiungendola alla fine, dopo qualunque altro testo scritto in precedenza nel file.

Usando il metodo write si possono anche scrivere, nel file, stringhe a cui viene applicato un formato specifico, nel solito modo:

```python
file_modifica.write(‘Number of entries: %d\nTotal: %8.2f\n’ % (count, total))
```

In alternativa, si può scrivere testo in un file usando la funzione print. Basta fornire l’oggetto che rappresenta il file mediante un argomento di nome file:

```python
file_modifica = open(‘output.txt’, ‘w’)
print(“Hello, World!”, file= file_modifica)

#Se non si vuole andare a capo dopo il testo che viene scritto, 
#si usa l’argomento end:

print(“Hello, World!”, end=“”, file= file_modifica)
```

### Chiudere un file

Dopo aver terminato l’elaborazione di un file, bisogna accertarsi che questo venga chiuso, usando il metodo close:
```python
file_modifica.close()
```
Se il programma termina senza aver chiuso un file che era stato aperto per la scrittura, può darsi che alcuni dati scritti dal programma non siano stati effettivamente memorizzati nel file.

## *Leggere l'intero file*

### Leggere l'intero file assegnandolo a un'unica stringa

Il metodo read legge caratteri di testo a partire dalla posizione del cursore e permette anche di specificare il numero di caratteri da leggere.

```python
>>> fhand = open('mbox-short.txt')
>>> inp = fhand.read()
>>> print(len(inp))
94626
>>> print(inp[:20])
From stephen.marquar

#allora il metodo read restituisce una stringa
#contenente il successivo carattere disponibile nel file,
#oppure, se è stata raggiunta la fine del file,
#restituisce una stringa vuota, “”.

#Notare che, se è presente, viene letto anche il
#carattere “\n”.
```

### Leggere il file riga per riga

```python
handle = open("sintomi1.txt", 'r')
line = handle.readline()
```

* Quando un file viene aperto, un apposito contrassegno o cursore (marker) viene posizionato all’inizio del file stesso.
* Il metodo readline legge caratteri di testo a partire dalla posizione del cursore e continua fino a quando non incontra un carattere di “nuova riga” (newline \n) e restituisce il testo che ha letto, compreso il carattere di “\n”, sotto forma di unica stringa. Infine posiziona il cursore a capo.
```python
#File input.txt:
#Questa è una prova
#per vedere cosa succede
#Ad ogni nuova riga
#Grazie!

>>> handle = open("input.txt")
>>> line = handle.readline()
>>> print(line)
Questa è una prova
>>> line = handle.readline()
>>> print(line)
per vedere cosa succede
>>> line = handle.readline()
>>> print(line)
Ad ogni nuova riga
>>> line = handle.readline()
>>> print(line)
Grazie!
>>> line = handle.readline()
>>> print(line)
>>>
```

### Leggere un file riga per riga con il ciclo *for*

Posso usare un ciclo per leggere un file riga per riga(e in caso per elaborarne il contenuto) senza usare readline ma iterando sulle righe del file.

```python
fhand = open('input.txt')
count = 0
for line in fhand:
  print(line)
  count = count + 1
print(count)
```

**Output**:

"_Questa è una prova_

_per vedere cosa succede_

_Ad ogni nuova riga_

_Grazie!_

_4_"
___
## *Cercare all'interno di un file*

### Metodo con il ciclo for

```python
fhand = open('mbox-short.txt')
for line in fhand:
  if line.startswith('From:') :
    line = line.rstrip()
    print(line)
```

in alternativa:
```python
hand = open('mbox-short.txt')
for line in fhand:
  if not line.startswith('From:') :
    continue
  line = line.rstrip()
  print(line)
```

### Aprire file da "nome file" dato dall'utente
```python
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
  if line.startswith('Subject:') :
    count = count + 1
print('There werÈ, count, 'subject lines in', fname)
```

#### Gestire eccezioni relative al nome dei file

```python
fname = input('Enter the file name: ')
try:
  fhand = open(fname)
except:
  print('File cannot be opened:', fname)
  quit()
count = 0
for line in fhand:
  if line.startswith('Subject:') :
    count = count + 1
print('There werÈ, count, 'subject lines in', fname)
```
### Leggere parole elaborando da file

Quando elaboro file di testo, I metodi per stringhe e per liste sono molto utili. Posso usare il metodo split() per creare una lista.

```python
>>> line = 'A lot of spaces'
>>> etc = line.split()
>>> print(etc)
['A', 'lot', 'of', 'spaces']
>>>
>>> line = 'first;second;third'
>>> thing = line.split()
>>> print(thing)
['first;second;third']
>>> print(len(thing))
1
>>> thing = line.split(';')
>>> print(thing)
['first', 'second', 'third']
>>> print(len(thing))
3
>>>
```

Quando uso split e non specifico il carattere di delimitazione, spazi successivi sono trattati come uno solo. Naturalmente posso considerare caratteri alternativi per lo splitting. Se specifico l’argomento caratteri successivi non sono più trattati come uno solo.
___



# 6. Espressioni regolari

## Cosa sono le espressioni regolari
In computing, a regular expression, also referred to as “regex” or “regexp”, provides a concise and flexible means for matching strings of text, such as particular characters, words, or patterns of characters.

A regular expression is written in a formal language that can be interpreted by a regular expression processor.
| character | how it works |
| --------- | ------------ |
| ^ |Matches the beginning of a line|
|$ |Matches the end of the line|
|. |Matches any character|
|\s |Matches whitespace|
|\S |Matches any non-whitespace character|
|\d |Matches digit|
|\D |Matches any non-digit character|
|* |Repeats a character zero or more times|
|*? |Repeats a character zero or more times (non-greedy)|
|+ |Repeats a character one or more times|
|+? |Repeats a character one or more times (non-greedy)|
|[aeiou] |Matches a single character in the listed set|
|[^XYZ] |Matches a single character not in the listed set|
|[a-z0-9] |The set of characters can include a range|
|( |Indicates where string extraction is to start|
|) |Indicates where string extraction is to end|

Uso generale:
```python
import re
re.search() #returns match object
re.findall() #extracts portions of a string that matches regular expression
```
### find() 
```python
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  if line.find('From:') >= 0:
    print(line)
```
### re.search()
```python
import re

hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  y= re.search('From:', line) :
  if y is not None:
    print(line)
```
* The dot character matches any character
* If you add the asterisk character, the character is “any number of times”
* ^ => math the start of the line

WildCard Characters ex: _^X.*:_ => match any character zero or more times
WildCard Characters ex2: _^X-\S+:_ => match any non-whitespace character one or more times

Altro esempio:
```python
>>> import re
>>> x = 'My 2 favorite numbers are 19 and 42'
>>> y = re.findall('[0-9]+',x)
>>> print(y)
['2', '19', '42']
```

Quando usiamo ***re.findall()***, otteniamo una lista di zero o più sottostringhe che coincidono con le sotto-stringhe della nostra espressione regolare.

```python
>>> import re
>>> x = 'My 2 favorite numbers are 19 and 42'
>>> y = re.findall('[0-9]+',x)
>>> print(y)
['2', '19', '42']
>>> y = re.findall('[AEIOU]+',x)
>>> print(y)
[]
```

### Greedy Matching

The repeat characters (* and +) push outward in both directions (greedy) to match the largest possible string.

```python
>>> import re
>>> x = 'From: Using the : character'
>>> y = re.findall('^F.+:', x)
>>> print(y)
['From: Using the :']
```

### Non-Greedy Matching

Not all regular expression repeat codes are greedy! If you add a ? character, the + and * chill out a bit...


```python
>>> import re
>>> x = 'From: Using the : character'
>>> y = re.findall('^F.+?:', x)
>>> print(y)
['From:']
```

You can even go crazy on string extraction:

```python
>>> y = re.findall('\S+@\S+',x)
>>> print(y)
['stephen.marquard@uct.ac.za’]
```

There aremore details on the Regular Expressions slide. Look it up in case you need it.



# 7. Liste

## _Liste_

### Definizione

Le liste non sono altro che un'insieme di valori associati a un'unica variabile. Equivalente a mettere tante scatole dentro una scatola più grande, così da conservarci più elementi. In altri linguaggi di programmazione si chiamano _array_.

Un esempio di lista già utilizzato nel for sono gli indici di conteggio:

```python
for i in [5, 4, 3, 2, 1] :
  print(i)
print('Blastoff!')
```

Dichiarare una lista è semplice:

```python
friends = ['Joseph', 'Glenn', 'Sally']
```

Per usarla si possono usare singoli indici della lista in sé, o semplicemente usare un ciclo e facilitarsi la vita:

```python
z = ['Joseph', 'Glenn', 'Sally']
for x in z:
  print('Happy New Year:', x)
print('Done!')

#o semplicemente:

print(z[1])
```

-   Gli indici partono sempre da 0 a (lunghezzaLista-1). Superando il range si ottiene un _out-of-range error_.

*   In una lista si possono inserire elementi stringhe con interi e float senza particolari problemi.

*   Si possono usare indici negativi per le liste. _-1_ per esempio consente di accedere all'ultimo elemento della lista, _-2_ al penultimo e così via.

### Slicing

Possiamo selezionare solo parte di una lista da visualizzare o utilizzare, come con le stringhe:

```python
>>> t = [9, 41, 12, 3, 74, 15]
>>>
>>> t[1:3]
[41,12]
>>>
>>> t[:4]
[9, 41, 12, 3]
>>>
>>> t[3:]
[3, 74, 15]
>>>
>>> t[:]
[9, 41, 12, 3, 74, 15]
```

Se il secondo numero è maggiore della lunghezza della lista, Python non dà errore. Si ferma all’ultimo carattere. Mentre darebbe errore (out-of-range) se indicizzassimo _t[25]_.

#### Rispetto alle stringhe

Non si può modificare un valore indicizzato in una stringa, ma si può fare in un array:

```python
#stringhe
>>> fruit = 'Banana'
>>> fruit[0] = 'b'
Traceback
TypeError: 'str' object does not
support item assignment

#liste
>>> lotto = [2, 14, 26, 41, 63]
>>> lotto[2] = 28
>>> print(lotto)
[2, 14, 28, 41, 63]
```

### Lunghezza lista

_len()_ restituisce la lunghezza di una lista così come restituisce per le stringhe il numero di caratteri:

```python
>>> x = [ 1, 2, 'joÈ, 99]
>>> print(len(x))
4
```

### La funzione .range()

_range()_ è utile per sansionare una lista

```python
>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> print(len(friends))
3
>>> print(range(len(friends)))
[0, 1, 2]
>>>

#e lo si usa con i for:

friends = ['Joseph', 'Glenn', 'Sally']

for friend in friends :
  print('Happy New Year:', friend)

for i in range(len(friends)) :
  friend = friends[i]
  print('Happy New Year:', friend)
>>>
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
```

### Riferimento alla lista

Dichiarando la lista

```python
values=[32.54.67.5,29,35,80,115]
```

noi non memorizziamo effettivamente i numeri della racolta nella variabile. La variabile _values_ contiene invece un riferimento alla lista, cioè un indirizzo della posizione in memoria della lista.

-   Copiando una variabile in un'altra, di fatto viene copiato il riferimento di indirizzo alla lista. **Usando indiferentemente una lista o l'altra, si cambia il contenuto della stessa lista.**

```python
>>> scores = [10, 9, 7, 4, 5]
>>> values = scores # Copying list reference
>>> values == scores
True
>>> values is scores
True
```

### Copiare una lista con .list()

Per copiare una lista quindi, bisogna agire diversamente dal semplice assegnare x=y. Si usa _.list()_.

```python
>>> values = [10, 9, 7, 4, 5]
>>> prices = list(values)
>>> #controllo
>>> values == prices
True
>>> values is prices
False
```

#### Casi particolari:

```python
#lista dentro la lista
>>> a=[3,2,1]
>>> b=[a,4,5]
>>> b
[[3, 2, 1], 4, 5]
#ovviamente cambia il riferimento
#interno, e l'indice si riferisce alla
#lista completa di "a"
>>> cp=list(b)
>>> cp[2]
5
#e tra lettura e scrittura anche
>>> cp[2]=8
>>> cp
[[3, 2, 1], 4, 8]
>>> b
[[3, 2, 1], 4, 5]
#perciò bisogna fare attenzione
#particolare ai RIFERIMENTI INTERNI
>>> a[2]=0
>>> a
[3, 2, 0]
>>> b
[[3, 2, 0], 4, 5]
>>> cp
[[3, 2, 0], 4, 8]
```

### Concatenazione liste:

Si possono concatenare due liste usando l’operatore
**+**.

```python
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 5, 6]
```

Si può concatenare a ripetizione la stessa lista
usando l’operatore \*.

```python
>>> monthlyScores = [0] * 12
>>> print(monthlyScores)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

---

## _Metodi per liste_

### Funzioni che hanno argomenti di tipo _list_:

```python
>>> nums = [3, 41, 12, 9, 74, 15]
>>> print(len(nums)) #lunghezza
6
>>> print(max(nums)) #massimo
74
>>> print(min(nums)) #minimo
3
>>> print(sum(nums)) #somma di tutti i valori
154
>>> print(sum(nums)/len(nums)) #media
25.6
```

Gli oggetti mutabili, come le liste, hanno metodi dedicati che mutano l’oggetto stesso.

### Aggiungere elementi in una lista

Si usa _.append()_.

```python
friends = []
friends.append("Harry")
friends.append("Bob")
friends.append("Cari")
friends.append("Emily")
```

E si ottiene:
|Indice|Valore|
|--:|:--:|
|[0]|"Harry"|
|[1]|"Bob"|
|[2]|"Cari"|
|[3]|"Emily"|

### Inserire elementi in una lista

Per inserire spostando elementi in una lista, basta usare _.insert()_.

```python
friends = ["Harry", "Emily", "Bob", "Cari"]
friends.insert(1, "Cindy") #inserisci a indice 1
```

Tutti gli elementi che stavano dall'indice 1 in su vengono spostati in su. Perciò "Emily" per esempio, ora sarà all'indice 2.

### Cercare elementi in una lista

Per una ricerca semplice (di presenza) basta usare l'operatore _in_. È un operatore logico che restituisce TRUE o FALSE e non modifica la lista.

```python
>>> some = [1, 9, 21, 10, 16]
>>> 9 in some
True
>>> 15 in some
False
>>> 20 not in some
True
>>>
```

Se invece si vuole fare una ricerca che restituisce anche l'indice, bisogna usare il metodo _index_.

```python
friends = ["Harry", "Emily", "Bob", "Cari", "Emily"]
n = friends.index("Emily") # Sets n to 1
```

Per evitare errori durante l'esecuzione, è fondamentale assicurarsi prima della ricerca dell'indice assicurarsi che l'elemento è presente nella lista.

```python
if “Cindy” in friends :
  n = friends.index(“Cindy”)
else :
  n = –1
```

### Rimuovere/Eliminare elementi in una lista
 
Un modo per eliminare elementi da una lista è utilizzare il metodo _pop_

```python
friends = ["Harry", "Cindy", "Emily", "Bob", "Cari","Bill"]
friends.pop(1)
```
Non solo rimuove l'elemento dalla lista, ma shifta l'indice di tutti gli elementi successivi per fare in modo che non rimangano "buchi".


Non solo viene eliminato, ma viene anche restituito. Questo ci permette di utilizzarlo/salvarlo durante l'eliminazione:
```python
>>> print(“The removed item is”, friends.pop(1))
The removed item is Cindy
```

*Un altro modo per eliminare elementi da una lista è utilizzare il metodo _remove_, il quale elimina un elemento dalla lista sulla base del suo valore piuttosto che della sua posizione.

```python
element = “Cari”
if element in friends :
  friends.remove(element)
```
Come per il metodo _index_ bisogna prima verificare l'esistenza dell'elemento, altrimenti ci viene restituito un errore.


### Ordinare elementi in una lista


#### Un modo per ordinare elementi da una lista è utilizzare il metodo _sort_.

```python
>>> friends = [ 'Joseph', 'Glenn', 'Sally' ]
>>> friends.sort()
>>> print(friends)
['Glenn', 'Joseph', 'Sally']
>>> print(friends[1])
Joseph
>>>
```

### Ordinare elementi in una lista

Vanno sostituiti i valori, certo, ma mai dimenticarsi di usare una variabile "tampone", temporanea, per salvare il dato che sta per essere sovrascritto. 
```python
temp = values[i]
values[i] = values[j]
values[j] = temp
```
## _Tabelle e matrici_
Python non dispone, nelle librerie native, di un tipo di dato specifico per la creazione di tabelle, ma si può creare una struttura tabulare bidimensionale usando le liste in modo opportuno.

Il frammento di codice seguente crea una tabella costituita da 7 righe e 3 colonne, adatta a memorizzare i dati delle mutazioni (0 = assente; 1 = presente) geniche di 7 pazienti (righe) su 3 differenti loci o posizioni
(colonne) del DNA.
```python
PAZIENTI = 7
LOCI = 3
mutazioni = [
[ 1, 0, 1 ],
[ 1, 1, 0 ],
[ 0, 0, 1 ],
[ 1, 0, 0 ],
[ 0, 1, 1 ],
[ 0, 1, 1 ],
[ 1, 1, 0 ]
]
```
Per accedere a uno specifico elemento di una tabella, bisogna specificare, in due coppie di parentesi quadre separate, il valore di due indici, che selezionano, rispettivamente, la riga e la colonna:

```python
>>> mutazionePaz4Locus3 = mutazioni[3][2]
0
```
Posso anche accedere alla riga della matrice
```python
>>> mutazionePaz4 = mutazioni[3]
[1, 0, 0]
```
Ma non posso accedere direttamente alla
colonna di una matrice.

Note: Esiste il modulo (non nativo) __numpy__ per l’uso e l’elaborazione delle matrici

## _Appendere argomenti/file al codice sorgente_

Quando bisogna fornire in riga di comando argomenti di opzioni o file direttamente al codice sorgente, come per esempio così:
```bash
$ Python3 prova.py –d input.txt pippo.txt
```
Bisogna tenere conto che gli argomenti forniti nella riga di comando giungono al programma all’interno della lista _argv_, definita nel modulo _sys_. E vanno prelevati in questo modo:

```python
from sys import argv
for i in range(len(argv)):
  print(argv[i])
```

```bash
$ Python3 prova.py –d input.txt pippo.txt

prova.py
–d
input.txt
pippo.txt
```
E quindi il programmatore deve, usando istruzioni if-elif, decidere cosa fare degli argomenti forniti da riga di comando e come processarli poi nel suo codice.


## _Tuple_

Le tuple sono come le liste, un tipo di contenitore di sequenze di valori. Ma una volta creata una tupla, a non possiamo più alterare il suo contenuto. 

Assegnando un valore all'indice _n_ riceveremo un "Traceback error"

Le tuple sono più efficienti, usano meno memoria, e python ci lavora con algoritmi più veloci. 

### Funzioni che si possono usare con le tuple: _count_, _index_.

Quando usarle? Quando si hanno sequenze temporanee di oggetti che non è necessario modificare.

### Assegnazione

```python
>>> (x, y) = (4, 'fred')
>>> print(y)
fred
>>> (a, b) = (99, 98)
>>> print(a)
99
```



# 8. Grafica

## Cosa usare per la grafica

I due moduli principali per questo corso sono **ezgraphics** e **tkinter**.

## ezgraphics


### Come usarlo

Scaricare dal sito il modulo [ezgraphics](http://ezgraphics.org/).
E poi importare il modulo nel file sorgente:
```python
>>> from ezgraphics import GraphicsWindow
>>> win = GraphicsWindow()
```
La nuova fi nestra verrà automaticamente visualizzata sullo schermo. Contiene un pannello (detto canvas) largo 400 pixel e alto 400 pixel (default)

>Quando viene creata una finestra grafica, viene restituito l’oggetto che la rappresenta e lo si deve memorizzare in una variabile

Per creare una finestra grafica avente un pannello della dimensione desiderata, possiamo specificarne le dimensioni (larghezza e altezza).

```python
>>> win = GraphicsWindow(500,300)
```
Quando si crea un oggetto di tipo GraphicsWindow viene automaticamente creato anche un oggetto di tipo GraphicsCanvas, i cui metodi (applicati all’oggetto canvas) consentono di accedere al pannello su cui disegnare.

```python
>>> canvas = win.canvas()
>>> canvas = canvas.drawRect(x=5,y=10, width=20, height=30)
```

```python
# Questo programma crea una finestra grafica e disegna un
# rettangolo, una linea e un ovale. Rappresenta lo schema
# da seguire per tutti gli altri programmi grafici.
from ezgraphics import GraphicsWindow
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawRect(x=5, y=10, width=20, height=50)
canvas.drawLine(x1=30, y1=30, x2=100, y2=500)
canvas.drawOval(x=300, y=300, width=50, height=50)
win.wait()
```

Il commando _win.wait()_ serve per evitare la terminazione immediata della finestra grafica.

### RGB

Ognuno dei tre colori (Red, Green, Blue)possono avere 255 valori, per un totale di 16'777'216 colori.
Es:
```
Nero    (0,0,0)
Rosso   (255,0,0)
Verde   (0,255,0)
Blu     (0,0,255)
Giallo  (255,255,0)
Grigio  (127,127,127)
Bianco  (255,255,255)
```
Per modificare il colore usato per disegnare, si utilizza una delle seguenti invocazioni di metodo:

```python
canvas.setOutline(red, green, blue)
canvas.setOutline(colorname)#valore stringa, tra le seguenti
```

>_“black” “magenta” “maroon” “pink” “blue” “yellow” “dark blue” “orange” “red” “white” “dark red” “sea green” “green” “gray” “dark green” “light gray” “cyan” “gold” “dark cyan” “tan”_

### Colore riempimento

```python
canvas.setFill(red, green, blue)
canvas.setFill(colorname)
```

### Outline
```python
canvas.setOutline()
```


### Testo

```python
canvas.drawText(50, 100, ‘Rettangolo’)
```


## tkinter


### Come usarlo


```python
>>> import tkinter
>>> pannello = tkinter.Canvas()
```
> * La funzione Canvas del modulo tkinter crea un oggetto che è una finestra grafica

Per creare una finestra grafica avente un pannello della dimensione e del colore desiderati, possiamo specificarne le dimensioni (larghezza e altezza) e il background


```python
>>> pannello = tkinter.Canvas(width = 500, height = 400, bg = ‘cyan')
>>> pannello.pack()
```
Il widget Canvas di Tkinter è un'area rettangolare in cui possiamo disegnare (ellissi, dischi, rettangoli, linee, ecc.), immergere immagini e testo o altri widget.
```python
>>> pannello = tkinter.Canvas(width = 500, height = 400, bg = ‘cyan')
>>> pannello.pack()
>>> pannello.create_oval(1, 1, 50, 50)
```

Esempio programma generico con tkinter:

```python
import tkinter

pannello = tkinter.Canvas(width = 600, height = 700, bg = 'cyan')
pannello.pack()

pannello.create_line(30, 30, 100, 300,fill="blue") #x1=30, y1=30, x2=100, y2=300
pannello.create_rectangle(5, 10, 205, 60, fill="red", outline="green", width=10)
#x1=5, y1=10 (angolo superiore sinistro), x2=205, y2=60
pannello.create_oval(300, 300, 350, 380) #x1=300, y1=300, x2=350, y2=380

pannello.mainloop()
```
* Se scrivo un programma devo aggiungere pannello.mainloop() (pannello è il nome della variabile oggetto tkinter.Canvas)
*  In mancanza di questo enunciato, il programma al termine farebbe scomparire immediatamente la finestra grafica dallo schermo, senza lasciare all’utente il tempo di vedere quanto è stato disegnato. Così invece aspetta che l’utente selezioni con il mouse il pulsante di chiusura.

### RGB, fill, outline, testo

Tkinter lavora con l'esadecimale invece che con valori decimali fino a 255.

```python
# Questo programma crea una finestra grafica e disegna un
# rettangolo, una linea e un ovale. Rappresenta lo schema
# da seguire per tutti gli altri programmi grafici.

import tkinter

pannello = tkinter.Canvas(width = 600, height = 700, bg = ‘#00ffff’ )
pannello.pack()

pannello.create_line(30, 30, 100, 300,fill=“#fff") #x1=30, y1=30, x2=100, y2=300
pannello.create_rectangle(5, 10, 205, 60, fill="red", outline="green", width=10)
#x1=5, y1=10 (angolo superiore sinistro), x2=205, y2=60
pannello.create_oval(300, 300, 350, 380) #x1=300, y1=300, x2=350, y2=380

pannello.create_text(250, 10, text = 'Rettangolo')#testo

pannello.mainloop()
```

### Immagini

```python
from tkinter import *
canvas = Canvas(width = 400, height = 400, bg = 'green')
canvas.pack()

# load the .gif image file
gif1 = PhotoImage(file = 'DECK\\10c.gif')
gif2 = PhotoImage(file = 'DECK\\1d.gif')

# put gif image on canvas
canvas.create_image(80, 100, image = gif1, anchor = NW)
canvas.create_image(250, 100, image = gif2, anchor = NW)
#put some text
canvas.create_text(80, 90, text='PC')
canvas.create_text(250, 90, text='MÈ)

canvas.mainloop()
```

#Modulo turtle, images, graphics nella slide BPy16_Classes_example



# 9. Insiemi e dizionari

## 9.1 *Insiemi*

Un insieme è un contenitore che memorizza una raccolta di valori univoci, che, diversamente da una lista, ha insiemi memorizzati in modo disordinato. Quindi non ci sono indici a cui ci si può appoggiare per ricercare elementi.

Ma dato che gli insiemi non devono preservare alcun criterio di ordinamento le operazioni sugli insiemi sono molto più veloci delle operazioni su liste.

### Come crearli

```python
cast = { “Luigi”, “Gumbys”, “Spiny” }
```

con *set* si può convertire una sequenza in un insieme:

```python
>>> names = ['Luigi', 'Gumbys', 'Spiny']
>>> set(names)
{'Spiny', 'Luigi', 'Gumbys'}
>>> set(names[1])
{'y', 'G', 'b', 's', 'u', 'm'}
```

> In Python non si può creare un insieme vuoto usando una coppia di parentesi  
> graffe, {}, senza elementi al proprio interno. Si usa, invece, la funzione set  
> senza argomenti:

```python
cast = set()
```

Per scandire i singoli elementi di un insieme si usa un ciclo *for*.

```python
>>>names = ['Luigi', 'Gumbys', 'Spiny']
>>>cast = set(names)
>>>for character in cast : print(character)
Gumbys
Spiny
Luigi
```

L’ordine con cui vengono visualizzati gli elementi è, in generale, diverso da quello usato durante la creazione dell’insieme. Quando si lavora con gli insiemi il fatto che questi non preservino l’ordinamento iniziale tra i propri elementi non è un problema, anzi: è proprio questa mancanza del requisito di ordinamento che rende possibile un’implementazione molto efficiente delle operazioni tra insiemi.

### Lunghezza

```python
numberOfCharacters = len(cast)
```

### Aggiungere elementi

```python
cast = set([“Luigi”, “Gumbys”, “Spiny”])
cast.add(“Arthur”)
```

> un insieme non può contenere elementi duplicati: se  
> tentate di inserire in un insieme un elemento che è già presente, l’operazione non ha alcun effetto

### Eliminare elementi

#### .discard()

```python
cast = set([“Luigi”, “Gumbys”, “Spiny”])
cast.add(“Arthur”)
cast.discard(“Arthur”)# elimina un elemento se questo esiste all’interno dell’insieme

#ma non ha alcun effetto se l’elemento dato non è un membro dell’insieme:
cast.discard(“The Colonel”) # Nessun effetto
```

#### .remove()

```python
cast.remove(“The Colonel”) # Solleva un’eccezione
```

#### .clear()

```python
cast.clear() # Ora cast ha cardinalità 0
```

### Sottoinsiemi

Un insieme è un sottoinsieme di un altro insieme se e solo se tutti gli elementi del primo insieme sono anche elementi del secondo insieme.

Il metodo .issubset() restituisce True o False per segnalare se un insieme è un sottoinsieme di un altro:

```python
>>> canadian = { “Red”, “White” }
>>> british = { “Red”, “Blue”, “White” }
>>> italian = { “Red”, “White”, “Green” }
>>>canadian.issubset(british) :
True
```

#### Uguaglianza

Si può anche verifi care se due insiemi sono uguali o diversi, usando gli operatori == e !=. Due insiemi sono uguali se e solo se hanno esattamente gli stessi elementi.

#### Unione di due insiemi

L’unione di due insiemi contiene tutti gli elementi che provengono dai due insiemi, dopo avere eliminato i duplicati. In python si usa il metodo *.union()*, il quale restituisce un nuovo insieme senza modificare nessuno dei due insiemi.

```python
inEither = british.union(italian) # L’insieme { “Blue”, “Green”, “White”, “Red” }
```

#### Intersezione e differenza

In Python, il metodo .intersection() genera l’intersezione di due insiemi.

```python
inBoth = british.intersection(italian) # L’insieme { “White”, “Red” }

```

In Python, il metodo .difference() genera la differenza di due insiemi.

```python
print(italian.difference(british)) # Visualizza { “Green” }
```

Quando si genera l’unione o l’intersezione di due insiemi, l’ordine in cui li si usa è ininfluente.

### Il programma [spellcheck.py](http://spellcheck.py)

```python
#Il programma seguente legge un file di testo (un vocabolario) e inserisce le parole
#in un insieme. Poi, legge tutte le parole presenti in un secondo file di testo e le
#inserisce in un secondo insieme. Infine, visualizza tutte le parole del secondo
#testo che non fanno parte del vocabolario: si tratta delle parole che potrebbero
#contenere errori ortografici.
from re import split
def main() :
  # Legge il vocabolario e il documento.
  correctlySpelledWords = readWords(“words”)
  documentWords = readWords(“alice30.txt”)
  #Visualizza tutte le parole del documento che non sono nel vocabolario.
  misspellings = documentWords.difference(correctlySpelledWords)
  for word in sorted(misspellings) :
    print(word)
def readWords(filename) :
  wordSet = set()
  inputFile = open(filename, “r”)
  for line in inputFile :
    line = line.strip()
    # Qualsiasi carattere diverso da a–z o A–Z delimita una parola.
    parts = split(“[^a–zA–Z]+”, line)
    for word in parts :
      if len(word) > 0 :
        wordSet.add(word.lower())
  inputFile.close()
  return wordSet

# Inizio del programma.
main()
```


## 9.2 Dizionari


### *Dizionario*

Il dizionario è come una "borsa" di valori non ordinati. Puoi accedere ai singoli valori attraverso la chiave univoca a cui è assegnato il valore.

Più chiavi possono avere lo stesso valore. Ma ogni chiave deve essere univoca.

---

### _Come crearli_
```python
borsa = dict()
```
in alternativa
```python
borsa = {}
```
---
### _Aggiungere elementi_

Basta definire la chiave e assegnarli un valore:
```python
borsa['soldi'] = 3 #in borsa, soldi=3
borsa['fazzoletti'] = 1 
print(borsa)
{'soldi':3, 'fazzoletti':75}
```
Aggiungere una chiave che esiste già solleva un'eccezione. Controllare prima che la chiave esiste già (vedere _in_ più giù).

---

### _Usare i valori di un elemento_

```python
borsa['soldi'] = borsa['soldi']+ 3 #aggiungo 3 al valore
print(borsa)
{'soldi':6, 'fazzoletti':75}
```

---
### _Eliminare coppie_
Serve usare il metodo _pop_:
```python
borsa.pop("Soldi")
```
Pop restituisce il valore memorizzato però, e questo può essere usato in un'altra variabile durante l'eliminazione stessa.
```python
>>> soldiInBorsa = borsa.pop("Soldi")
>>> soldiInBorsa
6
```
---
### _Iterare/Scandire gli elementi di un dizionario_
Un semplice ciclo for ci permette di usare tutto il contenuto del dizionario:

```python
contatti = {‘Anna': 475231244, ‘Marco': 3332175423, 'Giovanni': 045781032}
for key in contatti: #key prenderà come valore ogni singola chiave(il nome dei contatti)
	print(key)#qui viene stampata la chiave
	print(contatti[key])#mentre qui viene richiamato il valore della chiave (il nr. di tel.)
```
---


### _Verificare presenza di chiave nel dizionario_
In questo caso serve usare l'operatore _in_.

```python
>>> ccc = dict()
>>> 'csev' in ccc
False #questo valore booleano possiamo usarlo al bisogno
```

Un modo semplice per usare _in_:
```python
names={'Michael':10}
if "Michael" not in names:
	print("Michael is not here.")
else print("Michael is here")

#in alternativa:
name="Michael"
if name in names:
	print(name+" is in the dictionary.")
```

Classica eccezione quando viene richiamata una chiave non presente nel dizionario:
>Traceback (most recent call last):
>File "<stdin>", line 1, in <module>
>KeyError: 'csev'

---

### _Verificare presenza di chiave nel dizionario_
In questo caso serve usare l'operatore _in_.

```python
>>> ccc = dict()
>>> print(ccc['csev'])
#questa è l'eccezione sollevata quando una chiave
#non è presente in un dizionario
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 'csev'

#perciò usiamo IN:
>>> 'csev' in ccc
False
```
---

### _Metodo __get___
get() restituisce un valore di default (impostato dall'utente) quando non viene trovata la chiave passata come primo argomento.

Esempio:
```python
>>> macchine=dict()
>>> macchine['PorchÈ]=2
>>> macchine['Ferrari']=5
>>> macchine.get('Ferrari',0)
5
>>> macchine.get('Ford',0)
0
#perché 'Ford' non è una chiave presente nel dizionario, viene usato
#il valore di default
```

Esempio più complesso:
```python
#numero di occorenze di nomi in una lista
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names : #vengono presi i valori di names e assegnati a name
	counts[name] = counts.get(name, 0) + 1 #"0" è il default
	#viene generata/richiamata una chiave sulla base di name
	#viene assegnato a quella chiave il valore del get()
	#cioè il numero di occorenze memorizzati come valori
	#nel dizionario. Se la chiave non è stata generata prima
	#di questo ciclo, il valore sarà 0+1, cioè 1.
print(counts)
```
viene restituito:
```python
{'csev': 2, 'zqian': 1, 'cwen': 2}
```
---
### _Due variabili di iterazione_

Esempio:

```python
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for (aaa,bbb) in jjj.items() :
	print(aaa, bbb)
```
risultato
```python
jan 100
chuck 1
fred 42
```
---

### _Recuperare la lista di chiavi e valori di un dizionario_

Possiamo estrarre la lista di chiavi, di valori, o coppie (chiavi, valori) usando i seguenti metodi:
```python
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}

>>> print(jjj.keys()) #lista di sole chiavi
['jan', 'chuck', 'fred']

>>> print(jjj.values()) #lista di soli valori
[100, 1, 42]

>>> print(jjj.items()) #lista di tuple contenenti entrambi
[('jan', 100), ('chuck', 1), ('fred', 42)]
```

### _Tuple e operatori di confronto_

Si possono usare operatori di controllo con le tuple

```python
#fa un confronto tra il primo elemento della prima
#tupla e il primo elemento della seconda.
#se il primo elemento restituisce false, passa al
#secondo. Poi fa OR tra tutti i risultati.

>>> (0, 1, 2) < (5, 1, 2)
True
>>> (5, 1, 2) < (5, 1, 2)
False
>>> ( 'Jones', 'Sally' ) < ('Jones', 'Sam')
True
>>> ( 'Jones', 'Sally') > ('Adams', 'Sam')
True
```
---
### _Ordinare un dizionario rispetto a __key___

Usando il confronto di tuple appena citato, si possono ordinare le coppie (key,value) di un dizionario rispetto a _key_.
Viene usato anche il metodo _items()_ per estrarre la lista di tuple e la funzione _sorted_ per ordinare la lista.


```python
>>> d = {'c':10, 'b':100, 'a':22} #creo dizionario
>>> d.items() #visualizzo le tuple 
dict_items([('a', 10), ('c', 22), ('b', 100)])
>>> sorted(d.items())#ordino le tuple secondo chiave
[('a', 10), ('b', 100), ('c', 22)]
```

Posso anche usarlo in questa maniera:
```python
>>> for k, v in sorted(d.items()):
... print(k, v)
...
a 10
b 100
c 22
```

---

### _Ordinare un dizionario rispetto a __value___

Qua la facenda si complica. Bisogna inanzitutto creare una lista di tuple (__value,key__) usando un ciclo for, e poi ordinarlo. Nota bene però: bisogna creare una lista di tuple separata al dizionario. Nell'ordinamento per __key__ possiamo fare i furbi e non memorizzarla in una lista di tuple separate, per poterlo poi ordinare, ma ora c'è la complicazione del dover invertire _value_ e _key_. Quindi:
1) _sorted_ applicato al dizionario restituisce la lista delle chiavi ordinate.
3) la chiave deve essere univoca, perciò se invertiamo chiave e valore, non è detto che riusciamo a costruire un dizionario senza che sia sollevata un'eccezione.

```python
>>> d = {'c':10, 'b':100, 'a':22}
>>> tmp = list()
>>> for k, v in d.items() :
... tmp.append( (v, k) )
...
>>> print(tmp)
[(10, 'a'), (22, 'c'), (100, 'b')]
>>> tmp = sorted(tmp, reverse=True) #ordinamento decrescente
>>> print(tmp)
[(100, 'b'), (22, 'c'), (10, 'a')]
```

Viene usato anche il metodo _items()_ per estrarre la lista di tuple e la funzione _sorted_ per ordinare la lista.

---
### _Copiare i dizionari_

Come per le liste vale il fenomeno di aliasing. Cioè si ha un problema di memorizzazione dei dizionari quando si cerca di "copiarlo", perché invece di copiare i dati viene solo copiato il riferimento ai dati.

__Possiamo copiare i dizionari in questa maniera__:
```python
>>> ddd = {'coursÈ: 182, 'agÈ: 21}
>>> aaa=dict(ddd)
>>> ddd['coursÈ] = "EIP"
>>> ddd
{'coursÈ: 'EIP', 'agÈ: 21}
>>> aaa
{'coursÈ: 'math', 'agÈ: 21}
```


Esempio del problema:
```python
>>> ddd = {'coursÈ: 182, 'agÈ: 21}
>>> aaa = ddd
>>> ddd['coursÈ] = "math"
>>> ddd
{'coursÈ: 'math', 'agÈ: 21}
>>> aaa
{'coursÈ: 'math', 'agÈ: 21}
```



---



# 10. Funzioni


## _Definizione e invocazione_

```python
#definizione
def nomeFunzione(parametro):
  #fai qualcosa con parametro
  return varOutput #ritorni il valore di varOutput
```

- __Ogni funzione deve essere definita PRIMA di essere invocata__. Se non lo si fa, verrà sollevata un'eccezione.
- Una funzione può essere chiamata/invocata da un'altra funzione prima di essere stata definita
-   Le funzioni possono ricevere più argomenti, ma restituiscono sempre un solo valore/variabile (possiamo ovviare questo restituendo una lista, o tupla, ecc).
-   Le funzioni possono non avere argomenti (come per esempio _random()_) e possono non restituire alcun valore (ad esempio _print("ciao")_)
-   Le funzioni che vengono arrivano già "installate" in python si chiamano _primitive_.
-   Possiamo definire un numero illiminato di funzioni per risolvere i problemi più disparati.
- È possibile (ma sconsigliabile) definire una funzione all'interno di un'altra funzione.


N.B.: Una funzione definita, ma che non viene chiamata, è una funzione che non verrà eseguita!
```python
def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day.')
#non è eseguita finché non faccio:
print_lyrics()
```
---

## _Definire più parametri_


```python
def minus(a, b):
  res = a - b
  return res
  
x = minus(3, 5)
print(x)
>>> -2

x = minus(b=7, a=2)
print(x)
>>> 5
```
_a_,_b_ nell'esempio sopra sono _parametri_, cioè variabili che usiamo nella esecuzione della funzione. 
_3_ e _5_, _7_ e _2_ sono invece i _valori dell'argomento_ che diamo in input alla funzione durante la chiamata.

Possiamo usare parametri diversi tra di loro come tipi (stringhe, boolean, int, etc), ma è importante chiamare la funzione con argomenti in input che rispettano il medesimo ordine. 

---


## _Passaggio di parametri_
_Variabili parametro/Parametri formali_: le variabili che vengono create all'interno della funzione, alla sua invocazione, incaricate di ricevere gli argomenti
_Parametri effettivi_: valori forniti alla funzione nel momento dell'invocazione


```python
import math
def circonferenza(raggio): #'raggio':variabile parametro
	Circ=raggio*2*math.pi
	return Circ
	
r=4
risultato=circonferenza(r)#'r':parametri effettivi
print(“La circonferenza è:”,risultato)
```

- __I parametri e variabili delle funzioni nascono quando nasce la funzione (non quando viene definita) e muoiono alla fine della sua esecuzione.__

---

## _Utilizzo di liste come parametri_
__Dando una lista come argomento alla funzione, la funzione non riceverà la lista stessa, ma solo il suo riferimento!__ Perciò qui la località delle variabili, menzionata prima, non vale. 

Meglio evitare il return quando una funzione modifica una lista passata come argomento. Es:
```python
def multiply(values, factor) :
	for i in range(len(values)) :
		values[i] = values[i] * factor
	return value
```
Questa non è sbagliata, ma mi può portare facilmente a fare errori.

La soluzione migliore è quella di creare un'altra lista all'interno della funzione e fare return al riferimento di quella.

es: 
```python
def squares(n) :
	result = [ ]
	for i in range(n) :
		result.append(i * i)
	return result
```
---
## _Utilizzo di tuple come parametri_
Abbiamo visto che una funzione può restituire un unico valore. Posso però restituire più valori attraverso l’uso di un’unica tupla!

```python
def quadrato (lato) :
	perimetro = lato * 4
	area = lato * lato
	return (perimetro, area) # Restituisce una tupla.
```
----

## _Visibilità/Scope delle variabili_
- Le variabili all'interno di una funzioni sono invisibili al suo esterno
- Una variabile all'interno di una funzione è una variabile "locale".
- Una funzione non riesce a modificare direttamente le variabili esterni ad essa. Perciò posso usare come nomi per le variabili locali anche nomi di variabili esterni già presenti.
- Si possono usare __variabili globali__. Queste sono definite fuori dalle funzioni, e sono visibili a tutte le funzioni.

### _Variabili globali_

Le variabili globali vanno definite ancor prima delle funzioni che le useranno.

Esempio:
```python
balance = 10000 # Una variabile globale

def withdraw(amount) :
	global balance # Questa funzione aggiorna la variabile globale balance
	if balance >= amount :
		balance = balance – amount
```
In generale, usare variabili globali è una pessima idea. Quando più funzioni aggiornano variabili globali, prevedere il risultato può diventare difficoltoso. 
__Evitare di utilizzare le variabili globali a tutti i costi.__ 

----
## _Return_

- Il _return_ di una funzione termina immediatamente il flusso della funzione, interrompendolo in quel punto. Si possono perciò usare più _return_ nella propria funzione, con comportamento analogo al _break_.
- Se una funzione non ha cosa restituire, verrà restituito il valore speciale _None_. Conviene sempre controllare il return, anche per motivi di debugging.

Esempio di uso corretto:
```python
def cubeVolume(sideLength) :
	if sideLength >= 0 :
		return sideLength ** 3
	else :
		return 0
```
Ma viene comunque consigliato di usare un solo return all'interno della funzione:

```python
def cubeVolume(sideLength) :
	volume = 0
	if sideLength >= 0 :
		volume = sideLength ** 3
	return volume
```
----
## _Consigli per scrivere codice sfruttando le funzioni_

- Organizzare il codice del programma in una serie di chiamate a
funzioni che catturano la logica più che i dettagli implementativi.
- È bene non ripetere istruzioni, ma memorizzare il lavoro fatto per riutilizzarlo, per evitare ridondanza che va a incidere negativamente sull'efficienza del codice.
- Se qualcosa è troppo lungo e complesso lo posso suddividere in parti più piccole usando le funzioni.


----
## _Moduli_

A volte può essere utile creare un modulo proprio con funzioni da riutilizzare in programmi diversi. I moduli, di per sé, non sono altro che file _.py_ nei quali sono contenute le definizioni di funzioni già viste.

Esempio di modulo _circlefunctions.py_:
```python
def diametro(raggio):
	Diam=raggio*2
	return Diam
#...
#ecc
```
Esempio di import ed uso:
```python
>>> import circlefunctions as cf
>>> cf.diametro(4)
8
```
---

## _Documentazione automatica della propria funzione_

È sempre indicato commentare le funzioni, il loro scopo, il significato dei parametri e del valore restituito, oltre a eventuali requisiti specifici. È preferibile usare lo stile di documentazione usato da Java, anche perchè è riconosciuto da moltri strumenti di generazione automatica della documentazione, come Doxygen.

```python
## Calcola il volume di un cubo.
# @param sideLength la lunghezza di un lato del cubo
# @return il volume del cubo
def cubeVolume(sideLength) :
	volume = sideLength ** 3
	return volume
```

N.B.: i commenti vanno fatti per ogni funzione per funzionare.

----


## *Cos'è la ricorsione?*

La ricorsione consiste nella scomposizione di un problema in un insieme di problemi più semplici che si risolvono implementando diverse funzioni. In qualche caso si può anche scomporre in problemi più piccoli ma dello stesso tipo.

Ogni funzione ricorsiva **deve** avere un *caso base*. Per evitare un ciclo infinito che porterebbe all'esaurimento delle risorse di memoria, una funzione ricorsiva deve avere un caso base che viene  "raggiunto" per ogni input possibile.

Non si ha **mai** una ricorsione **infinita**. Anche perché il computer ha sempre bisogno di una certa quantità di memoria per tenere traccia di ogni nvocazione. Una ricorsione infinita si può avere se il problema non viene semplicifato, o se manca la gestione di un caso speciale che faccia terminare la ricorsione. 

### _Esempio ricorsione: sequenza di Fibonacci_

*Fib(n) = Fib(n-1)+Fib(n-2)*

La serie di Fibbonaci è una successione di numeri interi positivi in cui ciascun numero è la somma dei due precedenti.

I primi due termini sono per definizione:

- Fib(1) = 1
- Fib(2) = 1

Quindi la serie di Fibonacci ha una definizione ricorsiva:

- Fib(3) = Fib(2)+Fib(1) = 1+1 = 2
- Fib(4) = Fib(3)+Fib(2) = 2+1 = 3
- Fib(5) = Fib(4)+Fib(3) = 3+2 = 5
  
  ...


In Python:
```python
def Fib(n):
	if n<3:# caso base
		value=1
	else:
		vale=Fib(n-1)+Fib(n-2)
	return(value)
```

---

## _Itterativo o Ricorsivo?_

Quando esiste una soluzione iterativa, questa è più veloce ed occupa meno memoria.


---

## _Mappatura_

Applico una funzione a ciascun valore di una sequenza (come una tupla o una lista). 

```python
>>> word=['23','34','-43','2','81']
>>> numeri=map(int,words)#applico la funzione in a ciascun elemento di words
>>> numeri
<map object at 0x029EFF90>
>>> list(numeri)
[23,34,-43,2,81]
>>> words #la lista originale non cambia
['23','34','-43','2','81']
>>> 
```

---

## _Filtraggio_
Applico un predicato a ciascun valore di una sequenza (come una tupla o una lista). **Un predicato è una funzione che restituisce True o False.** Se il predicato restituisce True il valore passa il filtro, altrimenti no.

```python
>>> def pari(n): return n%2==0
>>> f = filter(pari,range(10))
>>> f
<filter object at 0x00267C70>
>>> list(f)
[0,2,4,6,8]
```

---
## _Riduzione_

Il modulo _functools_ include la funzione _reduce_ che chiede come argomento:
- una funzione di 2 argomenti
- una sequenza di valori

"Reduce" applica ripetutamente la funzione argomento a tutti i valori della lista (ad es. è utile per fare una sommatoria).

```python
>>> from functools import reduce
>>> def add(x,y): return x+y
>>> data=range(1,5)
>>> reduce(add,data)
10
```

---



# 11. Classi

## _Cosa sono le classi_
La programmazione orientata a oggetti permette di elaborare dati dividendo i problemi grandi in problemi più piccoli. Le classi sono come degli stampini, che permettno di creare più oggetti simili con metodi e attributi specifici. 

Quindi una classe definisce caratteristiche astratte di un oggetti incluso suoi attributi e le proprietà degli stessi e il suo comportamento (metodo). 

L'insieme degli attributi di un oggetto definiscono lo stato dell'oggetto.

Es. classe:
```
classe: Dog
attributi: razza, colorePelo, ecc.
metodi: abbaiare, sedersi, ecc.
```

Es. oggetto o istanza:
```
Lilly, è un'istanza della classe Dog, ed è un bassotto marone, ecc.
```
---
## _Metodi_

I metodi sono funzioni, competenze specifiche di un oggetto. Per esempio, un oggetto _Dog_ può magari abbaiare, _.bark()_, camminare, .walk(), ecc.

I metodi, a differenza delle funzioni, hanno bisogno di essere chiamati su uno specifico oggetto (un'istanza di una classe). Quindi non possiamo semplicemente chiamare il metodo della classe Dog! Bisogna prima creare un oggetto di tipo Dog per poterlo aviare.

```python
Lilly = Dog() #istanzio l’oggetto Lilly di classe Dog
Lilly.bark() # stampa “bau bau”
```

È facile indentificare i metodi disponibili per le variabili di Python (String, list, dict, ecc) usando "dir" nel IDLE:
```python
>>>x="abc"
>>>dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalizÈ, 'casefold', 'center', 'count', 'encodÈ, 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintablÈ, 'isspacÈ, 'istitlÈ, 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replacÈ, 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcasÈ, 'titlÈ, 'translatÈ, 'upper', 'zfill']

```

Si può invece usare "type" in questo stesso modo per identificare la classe:
```python
>>>x="abc"
>>>type(x)
<class 'str'>
```
__Quindi si può dire per esempio che il metodo _upper()_ è un metodo della classe str.__

---

## _Come definire una classe e i suoi metodi_

```python
## Modello di un contapersone
class Counter :
  n = 0
  ## Il metodo click() incrementa il contatore n
  def click(self) : #notate l’indentazione. Sono dentro la definizione della classe
    self.n = self.n + 1 #Attraverso self accedo agli attributi della classe

```

La variabile parametro __self__ fa sempre automaticamente riferimento all’oggetto specifico con cui il metodo è stato invocato.

---

## _Incapsulamento_

L’insieme di tutti i metodi messi a disposizione da una classe, con la descrizione del loro comportamento, è __l’interfaccia pubblica (public interface) della classe.__

Quando si lavora con un oggetto di una classe, non si sa come siano memorizzati i dati all’interno dell’oggetto stesso, o come siano realizzati i metodi. Ad esempio, non c’è bisogno di sapere come faccia un oggetto di tipo str a organizzare la propria sequenza di caratteri, o come un oggetto di tipo list memorizzi i propri elementi. __Mi basta sapere il nome dei metodi e come usarli__

_L’incapsulamento prevede di fornire l’interfaccia pubblica di una classe, mantenendo nascosti i dettagli realizzativi. **Le intestazioni delle definizioni dei metodi e i loro commenti costituiscono l’interfaccia pubblica** della classe, mentre **i dati e il corpo dei metodi ne sono l’implementazione privata**. Tutte le variabili di esemplare di una classe dovrebbero essere private._

Es:
```python
## Modello di un contapersone
class Counter : 	#publ
  n = 0			#priv
  
  ## il metodo click() incrementa il contatore n
  def click(self) :     #publ
    self.n = self.n + 1 #priv
    
  ## il metodo getValue() restituisce il valore del contatore
  def getValue(self) :  #publ
    return self.n	#priv
    
  ## il metodo reset() azzera il conteggio di questo contapersone.
  def reset(self) : 	#publ
    self.n = 0		#priv
```
Ogni oggetto contiene dei dati e dei metodi (funzioni specifiche per un certo tipo di oggetto) ma per usarlo ci basta conoscere i nomi e i parametri dei metodi, non come sono implementati.


**Tutte le variabili di esemplare di una classe dovrebbero essere private.** Per segnalarle come "private" in Python si ha la convenzone di dare alle variabili nomi che iniziano con un singolo carttere di sottolineatura. 
*È poi responsabilità degli utilizzatori della classe non violare tale riservatezza.*

Esempio applicato al programma di prima:
```python
## Modello di un contapersone
class Counter : 	
  _n = 0			
  
  ## il metodo click() incrementa il contatore n
  def click(self) :     
    self._n = self._n + 1 
    
  ## il metodo getValue() restituisce il valore del contatore
  def getValue(self) :  
    return self._n	
    
  ## il metodo reset() azzera il conteggio di questo contapersone.
  def reset(self) : 	
    self._n = 0		
```


---



## _Costruttori_

E’ **buona norma** inizializzare le variabili di esemplare usando un metodo speciale chiamato costruttore. Questo viene invocato automaticamente nel momento in cui viene creato un oggetto.

Python usa per il costruttore il nome ***\_\_init__***(nota il doppio underscore).

Come va usato il costruttore:
```python
class Counter:
	def __init__(self): #notare l'uso di "self"
		self._n=0 #è il primo riferimento alla variabile
				  #perciò viene creata con valore 0.
```
Quando il costruttore viene (automaticamente) invocato, alla costruzione di un nuovo oggetto, la variabile parametro self assume il valore di riferimento all'oggetto che sta per essere inizializzato. 

Senza il *self* nel costruttore, la variabile parametro self NON assume il valore di riferimento all'oggetto (attenzione quindi).

**Non invocare mai il costruttore dopo che l'oggetto è stato costruito.**
```python
register1.__init__() # Pessimo stile
```

In generale, non si dovrebbe mai invocare un metodo Python il cui nome inizia con un doppio carattere di sottolineatura: tutti tali metodi hanno uno scopo specifico, riservato all’interprete (in questo caso, quello di inizializzare un oggetto appena creato).



### *Argomenti di Default*

*Costruttori un po' più furbi:*
```python
class BankAccount:
	def __init__(self, initialBalance = 0.0 ) :
		self._balance = initialBalance
```		
In questo modo posso invocare la classe sia dandogli qualsiasi, sia senza dargli argomenti (e quindi con initialBalance=0.0).



```python
AlexBankAccount=BankAccount() # initialBalance=0
MichaelBankAccount=BankAccount(3000.0) #initialBalance=3000
```

Questi vengono chiamati **argomenti di default**. Si possono impostare anche per i singoli metodi/funzioni. E per tutti gli parametri del metodo:


```python
def readIntBetween(low = 0, high = 100):
...

readIntBetween(10)#equivale a readIntBetween(10,100)
#o specificando la variabile da sovrascrivere
readIntBetween(high=1000)#equivale a readIntBetween(0,1000)
```	




----

## _Metodi Accessor e Mutator_

Quando si esamina l'interfaccia pubblica di una classa, è utile catalogare i suoi metodi come _modificatori_ (mutator) o di _solo accesso_ (accessor).

Un metodo modificatore può apportare modifiche all'oggetto su cui agisce.

Un metodo di solo accesso NON apporta modifiche all'oggetto su cui agisce.

I _setter_ e _getter_ sono appunto anche essi metodi _accessor_ e _mutator_.


----
## _Variabili private/pubbliche_

- Tutte le variabili di esemplare dovrebbero essere private e quasi tutti i metodi dovrebbero essere pubblici.
- Le variabili di esemplare vanno manipolate SOLO attraverso i metodi.
- Metodi che sono da ausilio ad altri metodi ha senso progettarli come privati (usare sempre il carattere underscore per iniziare i loro nomi).


----
## _Come capire quali metodi si ha a disposizione_

La funzione "dir()" da sempre una lista dei metodi che un oggetto ha a disposizione (non la classe, ma un oggetto creato con quella classe).

Ricordarsi di **non usare** metodi con singoli o doppi segni di sottolineatura (underscore). 

N.B.: "non __usare__" != "non implementare"! Questi metodi vanno (ovviamente) implementati nella classe che magari state costruendo.


----
## _Metodi != Funzioni_

Seppure implementare un metodo sia un'attività molto simile all'implementazione di una funzione, vi è una differeza essenziale: _dall'interno del corpo di un metodo si ha accesso alle variabili di esemplare dell'oggetto su cui si agisce_ (per l'uso di "self"). Ma oltre al _self_, un metodo può avere altre variabili parametro.

```python
def addItem(self, price) : #come per es. price
	self._itemCount = self._itemCount + 1
	self._totalPrice = self._totalPrice + price
```

Successive variabili parametro devono essere fornite via richiamo dei metodi. 

```python
register1 = CashRegister()
register1.addItem(2.95)#viene assegnato a "price"
```

Quando un metodo ha bisogno di invocare un altro metodo sullo stesso oggetto su cui sta agendo, lo invoca sul parametro "self".

```python
def addRepItems(self, quantity, price) :
	for i in range(quantity) :
		self.addItem(price
```


Siccome Python è un linguaggio dinamico in cui le variabili vengono create durante l'esecuzione, non c'è modo di impedire al programmatore di creare variabili di esemplare in qualunque metodo della classe. Ma tutte le variabili di esemplare che vengono create nel costruttore rimangono e sono disponibili in tutti i metodo. Perciò vanno create tutte nel costruttore, o prendere l'abitudine di farlo.


----


## _Collaudare una classe_

Il collaudo verifica che una classe funzioni correttamente in isolamento, al di fuori di un programma completo. 
Si può fare sia da shell, in modo interattivo, provado i vari metodi pubblici di una classe, dopo averne creato un oggetto da usare, ma è scomodo ripetere la sequenza di istruzioni ogni vlta, perciò conviene sempre fare un _programma di collaudo_(test program), non dissimile da un semplice script che esegue i vari metodi della classe.

Le fasi tipiche da seguire per la creazione di un programma di collaudo:

1) Costruire uno o più oggetti della classe da collaudare.
2) invocare uno o più metodi
3) visualizzare uno o più risultati
4) Visualizzare i corrispondenti risultati previsti


*Esempio classe da collaudare:*
```python
class CashRegister :
	def __init__(self) :
		self._itemCount = 0
		self._totalPrice = 0.0
	## Aggiunge un articolo allo scontrino.
	# @param price il prezzo di questo articolo
	def addItem(self, price) : #notate che c’è un altro parametro oltre a self
		self._itemCount = self._itemCount + 1
		self._totalPrice = self._totalPrice + price
	## Ispeziona l’importo totale dovuto.
	# @return l’importo totale
	def getTotal(self) :
		return self._totalPrice
	## Ispeziona il numero totale di articoli registrati.
	# @return il numero di articoli
	def getCount(self) :
		return self._itemCount
	## Azzera il numero di articoli e l’importo totale.
	def clear(self) :
		self._itemCount = 0
		self._totalPrice = 0.0
```
*Esempio programma collaudo:*
```python
## Questo programma collauda la classe CashRegister.
from cashregister import CashRegister
register1 = CashRegister()
register1.addItem(1.95)
register1.addItem(0.95)
register1.addItem(2.50)
print(register1.getCount())
print(“Expected: 3”)
print(“%.2f” % register1.getTotal())
print(“Expected: 5.40”)
```
*Risultato:*
```python
Esecuzione del programma
3
Expected: 3
5.40
Expected: 5.40
```

----
## _Variabile di classe_

A volte capita che un attributo appartenga più propriamente a una classe, piuttosto che a uno qualsiasi dei suoi oggetti.
In questo caso si usa una *variabile di classe*, chiamata anche *variabile statica* in altri linguaggi di programmazione.

Esempio: classe di conti bancari che usano tutti un numero di conto univoco, ma sequenziale. Primo utente nr. 1000, il secondo 1001, il terzo 1002 e così via mano a mano che vengono aperti conti correnti. In questo caso possiamo usare una variabile _lastAssigned che memorizzi l'ultimo valore dato, indipendentemente dagli oggetti generati.

*Come creare la variabile di classe:*

```python
class BankAccount :
	_lastAssigned = 1000 # variabile di classe PRIVATA
	
	def __init__(self, initialBalance = 0.0 ) :
		self._balance = initialBalance
		BankAccount._lastAssigned = BankAccount._lastAssigned + 1
		self._accountNumber = BankAccount._lastAssigned
```

Indipendentemente dal numero di oggetti generati con una classe, ci sarà sempre solo una copia di ogni specifica variabile di classe che viene definita al suo interno. Sta a essere inteso che dunque tale variabile è posizionata in una zona di memoria al di fuori di ogni oggetto generatovi.

----

## _Tenere traccia degli oggetti_

paragrafo 9.8 del testo consigliato

```python
```
----


## _Schemi ricorrenti_

- metodi che aggiungono o tolgono quantità da un totale
- metodi che azzerano una quantità da un totale
- metodi che impostano un valore rispetto a un default
- contatori (contano aggiunte o rimozioni)
- collezionare valori in una lista
- descrivere stati in base a valori
- gestire caratteristiche di un oggetto e inspezionarle

esempi di implementazioni nella slide BPy16, classi parte 2

```python
```
----
## _Vita di un oggetto_

- l'oggetto rimane vivo finché al suo interno esiste almeno una variabile oggetto che vi si riferisce.
- Quando non esiste più alcun riferimento a un dato oggetto, questo sarà prima o poi eliminato dal _garbage collector_
- Può anche essere eliminato manualmente definendo esplicitamente il metodo speciale *\_\_del__*:

```python
def __del__(self):
	print("I am destructed",self.x)
```
*implementazione:*
```python
class PartyAnimal:
	def __init__(self):
		self._x = 0
		print('I am constructed')
	def party(self) :
		self._x = self._x + 1
		print('So far', self._x)
	def __del__(self):
		print('I am destructed', self._x
```
*esecuzione*
```python
>>> an = PartyAnimal()
I am constructed
>>> an.party()
So far 1
>>> an.party()
So far 2
>>> an = 42 #sovrascrivo la variabile
I am destructed 2
>>>print(an)
42
```
Così facendo viene liberata subito la memoria.

----
## _Aliasing e riferimento self_

Una variabile di istanza di una classe non conserva al suo interno un oggetto, ma solo la posizione in memoria dell'oggetto. Questa posizione viene chiamata _"riferimento a oggetto"_ in gero tecnico, e quando una variabile memorizza la posizione di un oggetto nella memoria diciamo che "si riferisce" o "fa riferimento" a tale oggetto.

**Quando una variabile contiene un riferimento a oggetto e assegnamo al suo valore un'altra variabile, creiamo un _alias_, non una copia dell'oggeto.** Solo l'indirizzo viene copiato. 

Due variabili che fanno riferimento al medesimo oggetto vengono a volte chiamate alias perchè possiamo usare l'una o l'altra per modificare l'oggetto.


Per verificare se due variabili sono un _alias_ basta usare gli operatori ***is*** e ***is not***.


```python
>>> import copy
>>> register1 = CashRegister()
>>> register2 = register1
>>> register2 is register1
True
```


----
## _Copiare un oggetto_

Si usa la funzione **copy()** del modulo *copy*:

```python
register1 = CashRegister()
import copy
register3 = copy.copy(register1)
```
Come per le liste però, se una variabile di esemplare all'interno di un oggetto contiene a sua volta un indirizzo a un oggetto, potrebbero sorgere dei problemi.
In questi casi conviene fare il *deepcopy()*:
```python
register1 = CashRegister()
import copy
register3 = copy.deepcopy(register1)
```

___



# 12. Debugging

Il debugger di Python, chiamato _pdb_ ("Python DeBugger"), può essere usato in mancanza di IDE che forniscono la funzione di debugging. Il debuggin consiste nella correzione di programmi, direttamente in fase di programmazione o nella fase di testing/finale del programma stesso.

---

## _Uso di Pdb_

Usando il comando per l'inizio della tracciatura, il programma si interrompe senza terminare alla rica a cui ho inserito il commando. A quel punto attenderà input dall'utente (commandi specifici di Pdv) prima di proseguire. In questa modalità di debugging posso vedere il valore assunto dalle variabili locali della funzione in cui mi trovo __durante l'esecuzione__, e leggere direttamente dalla RAM i valori.



```python
import pdb#importare il modulo
def removeFromSortedList(a) :
	i = 0
	while i < len(a) :
		pdb.set_trace()#qui iniziamo a tracciare
		#POSSO USARNE PIU' DI UNO PER PROGRAMMA
		count = 1 # quante repliche ci sono?
		while i + count < len(a) and a[i + count] == a[i] :
			count += 1
		if count < 3 : # ci sono meno di 3 repliche
			i += count
		else :
			for x in range(count) :
		a.pop(i)
removeFromSortedList([1,2,1,3,4,2,1,3])
```


----
## _Commandi Pdb_

Per leggere il valore delle variabili locali:
```python
nomevariabile
#in alternativa:
nomeVariabile p #"p" sta per "print"
```

```python
n #"next": leggi solo l'istruzione successiva
  #viene usato anche quando vengono chiamate
  #altre funzioni, e vogliamo eseguirle senza
  #la modalità di debugging
  
s #"subroutine": per entrare dentro una funzione
  #con la modalità debugging
  
i #ritorna il valore della riga dove stiamo eseguendo
  #codice in questo momento

r #"continue until return": esce dalla funzione corrente

q #"quit": esce dal debugger, però fa crashare 
  #il programma ignorando i messaggi di errore

c #continua l'esecuzione del programma fino al successivo
  #pdb.set_trace()
  
count = 5 #con molto sale, posso fare così per
          #modificare il valore delle variabili
```
- Premendo ENTER da solo, viene ri-eseguito l'ultimo comando.

----

# 13. Eccezioni

## _Cosa sono?_

Errori sollevati quando l'interpreta incontra una riga di codiche che non può essere eseguita o una circostanza inattesa.

Quando un'eccezione viene sollevata, il programma non continua con l'ennunciato successivo, ma con un gestore di eccezione (exception handler). Perciò nasce la ncessità di gestire l'eccezione in maniera oportuna per evitare la terminazione del programma.

La clausola _try_ contiene contiene il codice che possono provocare l'eccezione.
La clausola _except_ contiene contiene la gestione dell'eccezione.

Minimizzare sempre il numero di istruzioni nel blocco try.

In generale, **quando viene sollevata un’eccezione Python genera un oggetto di classe Exception**.

Vi sono un certo numero di eccezioni standard per segnalare molte tipologie di eccezioni. Prendere in considerazione il tipo di eccezione può permetterci di considerare enunciati try/except più articolati.

Mentre il blocco try contiene enunciati che possono provocare le eccezioni dei tipi che volete gestire, mentre ciascuna clausola except definita immediatamente dopo il blocco try contiene un gestore per uno dei tipi di eccezioni:

```python
try :
  filename = input(“Enter filename: “)
  infile = open(filename, “r”)
  line = infile.readline()
  value = int(line)
except IOError : #gestisce l'eccezione IOError.
  print(“Error: file not found.”)
except ValueError as ecc : #gestisce l'eccezione ValueError.
  print(“Error:”, str(ecc))
```
### Eccezioni specifiche e generiche

Se almeno una di queste eccezioni viene sollevata, la parte non ancora eseguita del blocco try viene ignorata. Verrà sempre e solo eseguito il la clausa except definita specificatamente per il tipo di eccezione sollevato. Per questo conviene aggiungere un'eccezione più generica per i casi diversi da quelli specificati:
```python
try :
  filename = input(“Enter filename: “)
  infile = open(filename, “r”)
  line = infile.readline()
  value = int(line)
except IOError : #gestisce l'eccezione IOError.
  print(“Error: file not found.”)
except ValueError as ecc : #gestisce l'eccezione ValueError e salvo l'oggetto nella vaiabile ecc.
  print(“Error:”, str(ecc)) #notare che "str" è un metodo speciale della classe ValueError.
  
except Exception as ecc2 : #gestisco un'eccezione generica
print(“Error:”, str(ecc2))
```
```
Le eccezioni più generiche vanno sempre elencate DOPO quelle specifiche.
```
## _finally_

Indipendentemente dal sollevamento di un'eccezione oppure no, è importante a volte eseguire comunque delle eccezioni, come per esempio la chiusura di un file. Per questo serve la clausola _finally_:
```python
try :
  outfile = open(filename, “w”)
  try :
    writeData(outfile)
  finally :# viene eseguita comunque indipendentemente da quel che succede nel blocco try
    outfile.close()
except IOError : #gestisce l'eccezione che si può sollevare nel chiudere un file mai aperto.
print(“Error: file not found.”)
```

Siccome è piuttosto frequente usare un enunciato try/finally per aprire e chiudee un file, Python mette a disposizione un'abbreviazione specifica:
```python
with open(filename, “w”) as outfile :
writeData(outfile)
```
L’enunciato _with_ apre il file di cui è dato il nome, assegna alla variabile outfile l’oggetto che lo rappresenta (un oggetto di tipo file) e lo chiude in automatico quando viene raggiunta la fine dell’enunciato, oppure se viene sollevata un’eccezione.


## _raise_

Fa sollevare un oggetto di tipo "RuntimeError" scritto dall'uttente.
```python
if amount > balance :
  raise ValueError(“Amount exceeds balance”) #costruito nuovo ogg. di tipo eccezione
balance = balance – amount #se viene sollevata l'eccezione, questa riga non viene eseguita
```

* Quando una funzione rileva un problema che non è in grado di risolvere, è meglio che sollevi un’eccezione piuttosto che cercare di sistemare le cose in modo impreciso.
* Supponiamo, ad esempio, che una funzione si aspetti di leggere un numero da un file, ma che il file non contenga un numero. In questo caso, usare semplicemente il valore zero, ad esempio, sarebbe una cattiva idea, perché nasconderebbe il problema e forse provocherebbe un problema diverso in un altro punto del programma.
* Al contrario, una funzione dovrebbe gestire un’eccezione soltanto se è veramente in grado di porre rimedio al problema, altrimenti il rimedio migliore è semplicemente quello di lasciare che l’eccezione si propaghi al proprio invocante, consentendole di essere catturata da un gestore più competente.

---


# 14. Ereditarietà

## *Cos'è*
Assieme al *incapsulamento* e *polimorfismo* è alla base della programmazione orientata agli oggetti, e consente il ***riutilizzo del codice***.


## *Principio di sostituzione (substitution principle)*
*Si può sempre usare un oggetto di una sottoclasse in un punto in cui è prevista la presenza di un oggetto della sua superclasse*.

Ergo, perché non dovresti usare "car" o "bike" invece che "vehicle"?

---


## 14.1 *Sottoclassi ed ereditarietà*

```python
#ChoicheQuestion eredita da Question, 
#dunque ne estende le funzionalità ed
#eredità le caratteristiche.

class ChoiceQuestion(Question)

```
* Una sottoclassa eredità **tutte le variabili di esemplare**.
* Una sottoclassa eredità **tutte i metodi che non sovrascrive**.
* Nella sottoclasse posso aggiungere altre variabili nuove a quelle di esemplare
* Nella sottoclasse posso sovrascrivere un metodo ereditato della superclasse, basta fornire un'implementazione nuova
* Posso aggiungere metodi nuovi.


**È buona regola non usare direttamente le variabili private di una classe o sottoclasse, ma accedere sempre e solo attraverso i metodi.**

E vale anche per l'utilizzo della variabile all'interno stesso della classe: usare i metodi creati ad-hoc per modificare/leggere la variabile.


## 14.2 Superclasse ***object***

In Python, se una classe non deriva esplicitamente da un'altra, allora deriva *implicitamente* dalla superclasse universale **object**. **Object** è privo di proprietà, ed è il modello dell'entità più astratta immaginabile.

Quindi si ha, per esempio:
*object > Question > ChoicheQuestion*


* usando "dir" possiamo identificare tutti i metodi della nostra classe e i metodi implementati da *object*. Esempio:

```python
>>> register1 = CashRegister()
>>> print(dir(register1))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_itemCount',
'_totalPricÈ, 'addItem', 'clear', 'getCount', 'getTotal']
```
## 14.3 Costruttori

* Il **costruttore** di una sottoclasse **può definire eplicitamente soltanto le variabili di esemplare proprie della sottoclasse**.
* Anche le variabili esemplare di una sottoclasse **devono** essere definite chiamando il costruttore della superclasse.
* I costruttori di entramble le classi (sotto e super) hanno lo stesso  nome, e cioè *\_\_init\_\_*.

```python
def __init__(self):
	#stuff here

```
Per distinguere tra l'uno e l'altro, si usa la funzione *super()* per fare riferimento alla superclasse e *self* per fare riferimento alla sottoclasse.
```python
def __init__(self):
	#il costruttore della superclasse va invocato
	#PRIMA della definizione delle proprie variabili
	#esemplare della sottoclasse.
	super().__init__() 
	self._choiches=[]
```

Se il costruttore della sottoclasse richiede argomenti, bisogna fornirli nel metodo *\_\_init\_\_*.
```python
class Question:
	def __init__(self,testoDomanda):
		self._text = testoDomanda
		self._answer=""
class ChoiceQuestion(Question):
	def __init__(self,questionText):
		super().__init__(questionText)
		self._choices=[]
```



## 14.4 Sovrascrivere un metodo (override)

Si modifica il comportamento di un metodo quando viene usato dalla sottoclasse.

**Per sovrascrivere un metodo bisogna definire una sottoclasse un metodo che ha la stessa *firma*** (stesso nome e stesso elenco di tipi dei parametri). Questo metodo "prevale" su quello ereditato dalla superclasse. 

**N.B.** : da non confondere con il "sovracarico".

Esempio:
```python
#Ovverride Question.display().
	def display(self):
		#richiamo comunque il metodo "display"
		#della superclasse per visualizzare la domanda
		super().display()
		#e poi stampo anche tutte le scelte di risposte
		for i in range(len(self._choices)):
			choiceNumber=i+1
			print("%d: %s" %(choicheNumber, self._choices[i]))
```

Attenzione!
```python
	def display(self):
		self.display() #da ricorsione infinita!
		[...]		
```

---

## 14.5 _Polimorfismo_
Posso creare un metodo che accetta come parametro una oggetto per intero, e usare i metodi di quella oggetto all'interno del metodo.

**Non si può fornire un oggetto di tipo superclasse laddove sia previsto un oggetto di tipo sottoclasse.**


Questo va bene:
```python
text = “In which year was Python first released?”
answers = [“1991”, “1995”, “1998”, “2000”]
correct = 1
first = ChoiceQuestion()
first.setText(text)
addAllChoices(first, answers, correct)

```
Ma non fare mai questo:
```python
first = Question()
first.setText(text)
addAllChoices(first, answers, correct)
```
Con quest'ultimo codice viene sollevata un’eccezione di tipo AttributeError perché *q* fa ora riferimento a un oggetto di tipo Question, ma la classe Question non definisce un metodo addAllChoice e non si può invocare un metodo con un oggetto la cui classe non abbia definito quel metodo.



L’invocazione di un metodo viene sempre determinata al momento dell’esecuzione sulla base del tipo effettivo dell’oggetto con cui il metodo viene invocato: si parla di **ricerca dinamica del metodo** (dynamic method lookup).

```python
def presentQuestion(q) :
	q.display()
	response = input(“Your answer: “)
	print(q.checkAnswer(response))
```

La ricerca dinamica del metodo da eseguire ci consente di manipolare in modo omogeneo
oggetti che sono esemplari di classi diverse: questa caratteristica si chiama **polimorfismo**
(polymorphism, dal greco “multiforme”). Chiediamo a più oggetti di assolvere a un determinato
compito e ciascuno lo fa a modo suo.


```python
# This program shows a simple quiz with two question types.

from questions import Question, ChoiceQuestion

def main() :
	first = Question()
	first.setText("Who was the inventor of Python?")
	first.setAnswer("Guido van Rossum")
	second = ChoiceQuestion()
	second.setText("In which country was the inventor of Python born?")
	second.addChoice("Australia", False)
	second.addChoice("Canada", False)
	second.addChoice("Netherlands", True)
	second.addChoice("United States", False)
	presentQuestion(first)
	presentQuestion(second)

## Presents a question to the user and checks the response.
# @param q the question
#
def presentQuestion(q) :
	q.display() # Uses dynamic method lookup.
	response = input("Your answer: ")
	print(q.checkAnswer(response)) # checkAnswer uses dynamic method lookup.

# Start the program.
main()
```

Il polimorfismo rende i programmi facilmente estendibili. 

Immaginate di voler disporre di un nuovo tipo di domanda che richiede di effettuare un calcolo, per il quale si vuole accettare anche una risposta approssimata.
Tutto ciò che dobbiamo definire è una nuova classe, *NumericQuestion*, che estenda Question e che abbia il proprio metodo *checkAnswer*


A questo punto possiamo invocare la funzione *presentQuestion* più volte, con un assortimento di domande normali, domande con opzioni e domande con risposta di tipo numerico. Non c’è alcuna modifica da fare alla funzione *presentQuestion*!

Grazie alla ricerca dinamica dei metodi, le invocazioni dei metodi *display* e *checkAnswer* selezionano automaticamente il metodo della classe giusta.

C'è un bel esempio sulla slide BPy19_Ereditarietà.pdf, da studiare

---


## _Classi e metodi astratti_

Definendo un metodo che non fa nulla e il programmatore ne definisce una nuova sottoclasse, bisogna ricordarsi di sovrascriverla, altrimenti il metodo ereditato non farà alcunchè.

Per questo possiamo segnalare un metodo come astratto, cioè non è effettivamente implementato.  Questo costringe i progettisti di una sottoclasse a fornire un’implementazione concreta del metodo.

In Python, non c’è un modo esplicito per specificare che un metodo è astratto, quindi i programmatori realizzano questo comportamento progettando un metodo che, come propria unica azione, solleva un’eccezione di tipo *NotImplementedError*:

```python
## Carries out the end of month processing that is appropriate for this account.
def monthEnd(self):
	raise NotImplementedError
```
 In questo modo, se l’utente della classe tenta di invocare il metodo della superclasse verrà sollevata l’eccezione, segnalando l’implementazione mancante. Il motivo per cui si usano le classi astratte è quello di obbligare i programmatori a progettare sottoclassi


Una classe che contiene almeno un metodo astratto si chiama **classe astratta** mentre una classe che, al contrario, non contiene alcun metodo astratto si chiama **classe concreta**.

---

# 15. Algoritmi

## _Ricerca binaria/dicotomica/bisezione_

### _Algoritmo iterativo_

Si può fare **solo in una lista ordinata**. Il valoreDaCercare può anche essere una stringa, basta che si stia analizzando una lista di stringhe piuttosto che di valori (se non vuoi che partano eccezioni).

```python
   def ricBinariaIterat(lista, valoreDaCercare):

      low = 0
      high = len(lista) - 1

      while low <= high :
         mid = (low + high) // 2
         if lista[mid] == valoreDaCercare :
            return True ##Questo algoritmo dice solo Vero o Falso
            #Se serve l'indice dalla lista, basta fare "return mid"
         if lista[mid] < valoreDaCercare :
            low = mid + 1
         else :
            high = mid - 1
      return False#Se serve l'indice, si può fare un'eccezione
      #o "return -1", per dire che non è stato trovato,
      #ma ovviamente entrambi i casi vanno gestiti.
```
### _Algoritmo ricorsivo_

Si può fare anche esso **solo in una lista ordinata**. Il valoreDaCercare può anche essere una stringa, basta che si stia analizzando una lista di stringhe piuttosto che di valori (se non vuoi che partano eccezioni).
```python
def ricBinariaRicorsiva(lista, inizio, fine, valoreDaCercare):
     # l'algoritmo ritorna l'indice
     if inizio > fine:
      return -1
     if valoreDaCercare < lista[inizio] or valoreDaCercare > lista[r]:
      return -1

     q = (inizio+fine)/2

     if lista[q] == valoreDaCercare:
      return q
     elif lista[q] > valoreDaCercare:
      return ricBinariaRicorsiva(lista,inizio,q-1,valoreDaCercare)
     else:
      return ricBinariaRicorsiva(lista,inizio+1,fine,valoreDaCercare)
```

---

# 16. Analisi delle prestazioni e sorting
## Analisi delle prestazioni degli algoritmi
Per valutare l’**efficienza temporale** di un algoritmo si misura il tempo necessario alla sua esecuzione su insiemi di dati di dimensione crescente. Il tempo di esecuzionedipende dal numero e dal tipo di interazioni in *linguaggio macchina* e va misurto all'interno del programma usando il metodo *time()* che a ogni invocazione restituisce un valore di tipo float. A noi interessa la differenza del tempo calcolato all'inizio e alla fine dell'esecuzione dell'algoritmo, altrimenti il valore verrebbe calcolato rispetto alla *mezzanotte del 1 gennaio 1970*. Il metodo si invoca come segue:
```python
from time import time
```

Per un'analisi teorica si **contano gli accessi in lettura/scrittura** a singoli elementi della lista (o le operazioni più onerose), ipotizzando che queste siano più lente. Si fanno **semplificazioni drastiche** ignorando tutto cià che non incide in modo significativo sul tempo, considerando solo operazioni elementari e trascurando input/output. Le prestazioni si calcolano **nel caso peggiore** (worst case) per avere una stima affidabile.

### Andamento asintotico delle prestazioni
L'andamento asintotico misura come cresce il tempo di esecuzione al crescere della dimensione dell'input *n*. Per confrontare algoritmi diversi, interessa sapere come cresce la funzione, cioè quale andamento qualitativo ha: si usa l’andamento asintotico che permette di valutare le prestazioni temporali in modo indipendente da fattori hardware.

Esiste una formulazione matematica del concetto "quale andamento ha una funzione di *n*, per *n* che tende all'infinito?".

### Notazione O-grande 
Una funione $f(n) \in O(g(n))$ se $\exists c>0$ e $k>0$ tali che $f(n)<cg(n) \forall n \geq k$.

Al crescere di *n* prima o poi una funzione *g(n)* è sempre maggiore della funzione *f(n)* a meno di una costante moltiplicativa. $g(n)$ è detto anche **limite superiore asintotico** per $f(n)$. $f(n)$ è **O-grande** di $g(n)$. 

> Si usa il segno $\in$ perché $O(g(n))$ è un simbolo che rappresenta l’insieme di tutte le funzioni $f(n)$ che rispondono alla definizione per una determinata funzione $g(n)$. Spesso si scrive, impropriamente, $f(n) = O(g(n))$.

Si dimostra che una *funzione polinomiale* è O-grande del suo monomio di grado massimo, con coefficiente moltiplicativo arbitrario. Per semplicità, tale coefficiente viene assunto uguale a 1. 

La definizione implica che $f(n)$ sia O-grande di qualunque funzione che cresce più veloce di $g(n)$. A noi interessa la funzione "più stringente".

> Ad esempio, avendo $T(n) \in O(n^2)$, non è sbagliato dire che $T(n) \in O(n^3)$ perché $T(n) \in O(n^2) \subset O(n^3) \subset O(n^4) \subset \cdots$.

Ecco una lista di espressioni in notazione O-grande:
| Espressione O-grande | Nome         |
|----------------------|--------------|
| O(1)                 | Costante     |
| O(log n)             | Logaritmica  |
| O(n)                 | Lineare      |
| O(n log n)           | Log-lineare  |
| O(n²)                | Quadratica   |
| O(n³)                | Cubica       |
| O(2ⁿ)                | Esponenziale |
| O(n!)                | Fattoriale   |


### Notazione Omega
Una funzione $f(n) \in \Omega(g(n))$ se $\exists c>0$ e $k \geq 1$ tali che $f(n) \geq g(n) \forall n\geq k$.

Prima o poi $f(n)$ cresce più velocemente di $g(n)$ e, quindi, $g(n)$ è un **limite inferiore** asintotico per $f(n)$. $f(n)$ è **Omega** di $g(n)$. 

Si dimostra che una funzione polinomiale è $\Omega$ del suo monomio di grado massimo, con coefficinete moltiplicativo arbitrario.

### Notazione Theta
Una funzione $f(n) \in \Theta(g(n))$ se $f(n) \in \Omega(g(n))$ e $f(n) \in O(g(n))$.

Prima o poi $f(n)$ e $g(n)$ crescono alla stessa velocità. $f(n)$ è **Theta** di $g(n)$

Si dimostra che una una funzione polinomiale è $\Omega$ del suo monomio di grado massimo, con coefficiente moltiplicativo arbitrario. 

> La caratterizzazione mediante $\Theta$ è la più precisa e utile, ma è difficile da calcolare. Si usa la notazione O-grande fornendo la stima più precisa possibile di $g(n)$


## Ordinamento per selezione (Selection Sort)
L’**ordinamento per selezione** è un algoritmo semplice ma poco efficiente.
L’idea di base è individuare, ad ogni passo, l’elemento più piccolo nella parte non ancora ordinata della lista e scambiarlo con l’elemento in prima posizione della parte da ordinare.

```python
def selectionSort(values):
    for i in range(len(values) - 1):
        minPos = minimumPosition(values, i)
        # scambia i due elementi
        temp = values[minPos]
        values[minPos] = values[i]
        values[i] = temp

def minimumPosition(values, start):
    minPos = start
    minVal = values[minPos]
    for i in range(start + 1, len(values)):
        val = values[i]
        if val < minVal:
            minPos = i
            minVal = val
    return minPos

```

### Prestazioni dell'algoritmo
Facendo ipotesi semplificative e contando soltanto gli accessi a singole celle della lista, le prestazioni temporali asintotiche validate (cioè verificate sperimentalmente) sono:
  - *Caso migliore*: **$O(n^2)$** (non è necessario fare scambi).
  - *Caso peggiore*: **$O(n^2)$**.
  - *Caso medio*: **$O(n^2)$** perchè lo è sia nel caso peggiore, che in quello migliore.

L'algoritmo è anche **$\Omega(n^2)$** e **$\Theta(n^2)$**.


## Ordinamento per inserimento (Insertion Sort)
L’algoritmo **Insertion Sort** è un algoritmo di ordinamento semplice ed efficiente per piccoli dataset o liste quasi ordinate. Funziona costruendo gradualmente una sottolista ordinata, inserendo un elemento alla volta nella sua posizione corretta all’interno della sottolista stessa. Ogni nuovo elemento viene spostato verso sinistra finché non si trova nella posizione corretta.

```python
def insertionSort(values):
    for i in range(1, len(values)):
        next = values[i]

        # sposta tutti gli elementi più grandi verso l'alto
        j = i
		while j > 0 and values[j - 1] > next:
			values[j] = values[j - 1]
			j = j - 1

		# inserisci il prossimo elemento
		values[j] = next

```

### Prestazioni dell'algoritmo
Le prestazioni temporali asintotiche validate sono:
  - *Caso migliore*: **$O(n)$** (lista già ordinata).
  - *Caso peggiore*: **$O(n^2)$** (lista ordinata in modo inverso).
  - *Caso medio*: **$O(n^2)$** (si richiede lo spostamento di metà degli elementi a sinistra).

L'algoritmo è anche **$\Omega(n)$**. Non esiste una caratterizzazione di tipo $\Theta$ per l'algoritmo nel suo caso generale.


## Ordinamento per fusione (Merge Sort)
L'algoritmo  **Merge Sort** è un algoritmo di ordinamento basato sul paradigma "divide et impera". Divide la lista in due metà, ordina ricorsivamente ogni metà e poi fonde (*merge*) le due metà ordinate.

> NB: la fusione è una fase dell'ordinamento per fusione.
 
```python
def mergeLists(first, second, values):
    iFirst = 0  # Prossimo elemento da considerare nella prima lista
    iSecond = 0  # Prossimo elemento da considerare nella seconda lista
    j = 0  # Prossima posizione libera in values

    # Finché né iFirst né iSecond superano la fine delle rispettive liste,
    # sposta l'elemento più piccolo nella lista values
    while iFirst < len(first) and iSecond < len(second):
        f = first[iFirst]
        s = second[iSecond]
        if f < s:
            values[j] = f
            iFirst = iFirst + 1
        else:
            values[j] = s
            iSecond = iSecond + 1
        j = j + 1

    # Copia eventuali elementi rimanenti della prima lista
    while iFirst < len(first):
        values[j] = first[iFirst]
        iFirst = iFirst + 1
        j = j + 1

    # Copia eventuali elementi rimanenti della seconda lista
    while iSecond < len(second):
        values[j] = second[iSecond]
        iSecond = iSecond + 1
        j = j + 1

```


### Prestazioni dell'algoritmo
Le prestazioni sono $\Theta(n\cdot log(n))$, cioè è migliore di ogni algoritmo quadratico. Di conseguenza, possiamo dire che l'ordinamento per fuzione è ancue un $O(n\cdot log(n))$.

### Mege Sort iterativo
L'algoritmo Merge Sort per una lista si può realizzare in modo iterativo, con le stesse prestazioni. Ogni elemento è una lista di lunghezza 1, ciascuna coppia di elementi consecutivi viene fusa in una lista ordinata di lunghezza 2 e così via.

### Confronto di algoritmi
Se le notazioni di O-grande delle prestazioni di due algoritmi diversi sono tra loro *diverse*, è possibile dire qual è l'algoritmo migliore. Se le prestazioni sono *uguali*, bisogna tenere in considerazione anche i fattori trascurati; in mancanza di ciò, i due algoritmi sono **equivalenti**. 

Si dimostra che qualunque algoritmo di ordinamento che operi mediante confronti tra i valori da ordinare richiede, nel caso peggiore, un tempo che è $\Omega(n\cdot log(n))$.

Il processo decisionale di un algoritmo di ordinamento che opera per confronti si può rappresentare tramite **albero di decisione**: ogni nodo contiene una domanda del tipo $"a_i \leq a_j?"$, le foglie rappresentano una decisione. Si dimostra che tutti gli alberi di decisione che rappresentano un algoritmo di ordinamento che opera mediante confronti su una sequenza contente $n$ elementi distinti, hanno almeno $n!$ foglie.


## Quick sort
L'algoritmo **Quick Sort** è un algoritmo di ordinamento basato sul paradigma "divide et impera". Sceglie un elemento come "pivot" e partiziona la lista in due parti: una con elementi minori e una con elementi maggiori del pivot. Ordina ricorsivamente le due parti senza aver bisogno di liste temporanee per ordinare. 

Nella variante più semplice delll'algoritmo, si sceglie come pivot il primo elemento della porzione. 

```python
def quickSort(values, start, to):
    if start >= to: return
    p = partition(values, start, to)
    quickSort(values, start, p)
    quickSort(values, p + 1, to)

# Partiziona una porzione di una lista
def partition(values, start, to):
    pivot = values[start]
    i = start - 1
    j = to + 1
    while i < j:
        i = i + 1
        while values[i] < pivot:
            i = i + 1
        j = j - 1
        while values[j] > pivot:
            j = j - 1
        if i < j:
            temp = values[i]
            values[i] = values[j]
            values[j] = temp
    return j

```

### Prestazioni dell'algoritmo
La scelta del pivot influenza le prestazioni dell'algoritmo. Se il pivot è l'*elemento mediano* della lista, le prestazioni saranno $\Theta(n\cdot log(n)$; se invece il pivot è l'ultimo elemento di una sequenza già ordinata, le prestazioni saranno $\Theta(n^2)$ nel caso peggiore.

Il caso peggiore si verifica quando il pivo è sempre il più piccolo o il più grande elemento. La complessità diventa $\Theta (n^2)$.

Il caso medio si ha se il pivot viene scelto in modo casuale. La complessità diventa $O(n\cdot log(n))$.

### Confronto con Merge Sort
L'algoritmo Merge Sort ha sempre prestazioni $O(n\cdot log(n))$, ma richiede spazio aggiuntivo. Quick Sort è sempre più veloce di Merge Sort, ma può egenerare a $\Theta(n^2)$ nel caso peggiore.


## Ricerca di un elemento
Data una lista di dati **non ordinati**, per fare una ricerca in essa ci sono due possibili soluzioni. 

  - **Ricerca lineare**: esamina tutti i valori di una lista finche non trova una corrispondenza con quanto cercato oppure giunge alla fine. I valori sono trovati in un numero di passi $O(n)$.
```python
def linearSearch(values, target):
  for i in range(len(values)):
	if values[i] == target:

  return -1
```
	
  - **Ricerca binaria o per bisezione**: cerca un valore in una lista ordinata determinano se si trovanella prima o nella seconda metà della lista stessa, ripetendo la ricerca in una sola delle due metà. È un algoritmo $O(log(n))$.
```python
def binarySearch(values, low, high, target):
if low <= high:
	mid = (low + high) // 2

	if values[mid] == target:
		return mid
	elif values[mid] < target:
		return binarySearch(values, mid + 1, high, target)
	else:
		return binarySearch(values, low, mid - 1, target)
else:
	return -1
```

Senza ordinare la lista, per effettuare la ricerca di un elemento occorre un tempo $O(n)$: si preferisce non ordinare la lista se bisogna fare una sola ricerca. Se invece bisogna fare molte ricerche, è meglio ordinare e usare la ricerca bianaria. 


# 17. Strutture dati
Una **struttura dati** è un modo organizzato di memorizzare e gestire i dati in memoria per consentire accesso ed elaborazione efficienti. In Python, le strutture sequenziali principali sono: *liste*, *tuple* e *stringhe*.

Un **array** è una rappresentazione dei dati in cui un insieme è memorizzato uno dopo l'altro in porzioni contigue della memoria e di uguale dimensione. Conoscendo l'indirizzo di memoria nel quale inizia l'array (*start*) e la dimensione di ogni cella (*cellsize*), l'indirizzo di memoria di ogni elemento dell'array è calcolarto come:
```
start + cellsize*index
```

La stessa dimensione di ogni cella permette un accesso diretto in un tempo costante $O(1)$. 

Dal momento che le stringhe sono memorizzate come sequenza ordinata di caratteri (character), una stringa può essere memorizzata in un array.

## Referential array
Nel caso di elementi memorizzati di dimensione diversa, come nel caso di liste e tuple, la memorizzazione avviene tramite **riferimenti** a *celle sparse*. Vengono memorizzate in celle consecutive gli indirizzi delle porzioni di memoria (non necessariamene consecutivi) in cui sono contenuti gli elementi della lista/tupla.

### Puntualizzazione rispetto ad aliasing, shallow copy e deep copy
  - Nell'*aliasing* tutte le modifiche effettuate su una lista agiscono anche sull'altra e viceversa.
  - In una *shallow copy* tutte le modifiche effettuate in una delle due liste agiscono sugli indirizzi memorizzati nell'array, non sugli integer.
  - Im una *deep copy* tutte le modifiche a una lista non hanno alcun effetto sull’altra, né sulla struttura né sui dati interni.

### Array compatti
Gli **arrray compatti** memorizzano anche i dati e non solo i riferimenti, come per le liste e le tuple. Una struttura che usa array di riferimenti occupa lo spazio per i riferimenti, più lo spazio per i dati. Per costruire array compatti si utilizza la *classe array* del *modulo array*. 
```python
from array import array
primes = array('i', [2, 3, 5, 7, 9, 11, 13, 17, 19])
```

### Array dinamici
Nel caso di stringhe e tuple (immutabili), la dimensione dei dati è immutabile; nel caso di liste (mutabii) la memoria deve essere collocata in maniera dinamica. Quando viene creata una lista, Python riserva spazio aggiuntivo per operzioni di append. Quando lo spazio finisce, viene allocata memoria per un nuovo array più grande, i riferimenti vengono trasferiti e il vecchio array abbandonato.

Il ridimensionamento di un array  è un operazione del tipo $\Theta(n)$. 

Il ridimensionamento per inserimento con costante moltiplicativa avviene in un tempo medio di tipo costante per la singola operazione, cioè $\Theta(1)$. Facendo un ridimensionamento con costante additiva, invece, il tempo medio è di tipo $\Theta(n)$. 

## Inserimenti e rimozioni in un array
L'inerimento e la rimozione richiedono sempre un ridimensionamento di un'unità nel caso di array "tutto pieno", altrimenti provocano una modifica della dimensione logica se l'array è "riempito solo in parte".

### Rimozione di un elemento
L'eliminazione di un elemento da un array richiede due algoritmi diversi:
  - Se l'ordine **non è importante**, si copia l'ultimo elemento nella posizione dell'elemento da eliminare e ridimensionare l'array fisicamente o logicamente.
    - Si richiedono due accessi e l'algoritmo viene eseguito in un *tempo costante* $\Theta(1)$. Il numero di accessi non dipende dalla dimensione dell'array.
    - In modalità "tutto pieno" il ridimensionamento costa $\Theta(1)$ se dobbiamo ridurre la dimensione logica e $O(n)$ se dobbiamo ridurre la dimensione fisica.
  - Se l'ordine **è importante**, tutti gli elementi di indice maggiore di quello dell'elemento da rimuovere vanno spostati nella posizione di indice immeidatamente inferiore.
    - Si richiedono due accessi e l'algoritmo viene eseguito, in media, in un tempo $\Theta(n)$.
    - Nel caso peggiore l'algoritmo rimane $\Theta(n)$.
    - Nel caso migliore, cioè quando l'elemento da rimuovere si trova in fondo a un array riempito solo in parte, le prestazioni sono $\Theta(1)$.

### Inserimento di un elemento
L'inserimento di un elemento da un array richiede due algoritmi diversi:
  - Se l'ordine **non è importante**, si inserisce o'elemento in ultima posizione e ridimensionare l'array fisicamente o logicamente.
    - Se c'è spazio si richiede un solo accesso in scrittura e l'algoritmo viene eseguito in un *tempo costante* $\Theta(1)$.
    - In modalità "tutto pieno" l'inserimento costa $\Theta(n)$ perché è richiesto il ridimensionamento.
  - Se l'ordine **è importante**, tutti gli elementi di indice maggiore di quello della posizione voluta vanno spostati nella posizione di indice immeidatamente superiore.
    - Si richiedono due accessi e l'algoritmo viene eseguito, in media, in un tempo $\Theta(n)$.
    - Nel caso peggiore l'algoritmo rimane $\Theta(n)$.
    - Nel caso migliore, cioè quando l'elemento si inserisce in fondo a un array riempito solo in parte, le prestazioni sono $\Theta(1)$.



# 18. Metodi di istanza e di classe
I metodi visti per le classi (o ***metodi di istanza***) sono funzioni definite *dentro il corpo di una classe* e sono invocabili **solo su istanze** della classe in cui sono definiti o da cui sono ereditati. Il primo argomento è *`self`*: il riferimento *_all’istanza_** su cui il metodo è invocato.

I ***metodi di classe***, invece, sono funzioni definite *dentro il corpo di una classe* e sono invocabili utilizzando **direttamente il nome della classe**, seguito dal punto e dal nome del metodo (con eventuali argomenti passati tra parentesi).

```python
class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def xy(self):
        return (self._x, self._y)

    def delta(p1, p2):
        return ((p1.x() - p2.x())**2 + (p1.y() - p2.y())**2)**(1/2)

```



# 19. Pile e code
## Pila (stack)
Una **pila** è una struttura dati in cui l'ultimo oggetto che è stato inserito è il primo ad essere rimosso, secondo un comportamento di tipo **LIFO** (*Last In First Out*). L'unico oggetto ispezionabile è quello che si trova in cima alla pila. Non c'è modo di ispezionare l'intero contenuto della pila senza svuotarla ordinatamente (*accesso sequenziale distruttivo*). 

I metodi che caratterizzano la classe pila sono:
```python
class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.pop()
```

I metodi `pop` e `top` non possono essere invocati con una pila vuota. L'implementazione della lista è avvenuta tramite *adapter design pattern*, dove viene usata un'istanza privata di una classe già definita (*list*) e implementati i metodi della nuova classe usando i metodi della classe già esistente sull'istanza privata. 

### Prestazioni
L'operazione di `push` in una pila ha come prestazioni:
	- caso migliore: $\Theta(1)$ (non serve un ridimensionamento)
	- caso peggiore: $\Theta(n)$ (serve un ridimensionamento in cui la dimensione viene moltiplicata per un fattore costante indipendente dalla dimensione della pila)
	- caso medio: $\Theta(1)$. Nonostante il caso peggiore sia $\Theta(n)$, il costo del ridimensionamento viene "ammortizzato" su molte operazioni di push. In pratica, il costo elevato del ridimensionamento avviene raramente, quindi il costo medio per operazione rimane costante.

Le prestazioni di `pop` e `top` sono entrambe $\Theta(1)$.

## Coda (queue)
Una **coda** è una struttura dati in cui il primo oggetto che è stato inserito sarà il primo ad essere rimosso, secondo un comportamento di tipo **FIFO** (*First In First Out*). La coda può essere accorciata da un lato e allungata dall'altro: si parla di *dequeue* quando si estrae un elemento dalla coda e di *enqueue* quando si inserisce un elemento in coda. L'unico oggetto ispezionabile è il primo della coda. Non c'è modo di ispezionare l'intero contenuto della pila senza svuotarla ordinatamente (*accesso sequenziale distruttivo*). 

I metodi caratteristici sono:
  - `enqueue`: per inserire un dato alla fine della coda.
  - `dequeue`: per eliminare il dato che si trova all'inizio della coda. Non vuole parametri perché non si può chiedere l'eliminazione di un dato specifico.
  - `front` o `getFront`: per ispezionare il dato che si trova all'inizio della coda, senza estrarlo
  -  `is_empty`: per sapere se il contenitore è vuoto.
  -  `size` o `len` per conoscere in numero di oggetti contenuti.

L'implementazione consiste in un array riempito in parte, del quale vengono usate entrambe le estremità. All'estremo con indice massimo si inseriscono nuovi elementi, con eventuale ridimensionamento, quando necessario. All'estremo di indice zero si rimuovono/ispezionano gli elementi presenti. La rimozione rende il metodo $\Theta(n)$.

### Code ad implementazione circolare
L’implementazione di una coda richiede uno shift degli elementi dopo ogni dequeue, con costo $\Theta(n)$. La **coda circolare** è una struttura dati logica ( fisicamente in memoria vi è un array) in cui esistono due indici, *head* e *tail*, che indicano il primo elemento e l'ultimo. Il vantaggio consiste nella modifica della variabile *tail* ad ogni inserimento e nella modifica dell'indice *head* ad ogni eliminazione. 

L'implementazione consiste in un array riempito solo in parte, del quale vengono utilizzate entrambe le estremità. All'estremo con indice massimo (*tail*) si inseriscono nuovi elementi, con eventiuale ridimensionamento, quando necessario. All'estremo di indice zero (*head*) si rimuovono/ispezionano gli elementi presenti. La rimozione rende il metodo $\Theta(n)$.

Le prestazioni ottenute sono corrispondenti a quelle di una pila:
  - Ispezione: $\Theta(1)$.
  - Inserimento: $\Theta(1)$, in media.
  - Rimozione: $\Theta(1)$.

> NB: Il valore dell'indice *tail* potrà raggiungere ma non superare il valore dell'indice *head*, analogamente *head* non potrà superare *tail*. Per garantire questo si lascia sempre una casella vuota e far indicare a tail la prima posizione vuota, oppure utilizzare una variabile booleana per verificare se la coda contiene elementi. 

Di seguito la realizzazione di una coda circolare.
```python
import deep

class ArrayQueue:    # FIFO queue implementation using a Python list as underlying storage
    DEFAULT_CAPACITY = 10    # Moderate capacity for all new queues

    def __init__(self):    # Create an empty queue
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._head = 0

    def __len__(self):     # Return the number of elements in the queue
        return self._size

    def is_empty(self):    # Return True if the queue is empty
        return self._size == 0

    def first(self):    # Return (but do not remove) the element at the head of the queue.
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self._data[self._head]

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        answer = self._data[self._head]
        self._data[self._head] = None    # Help garbage collection
        self._head = (self._head + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):    # Add an element to the back of queue
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        tail = (self._head + self._size) % len(self._data)
        self._data[tail] = e
        self._size += 1

    def _resize(self, cap):    # Resize to a new list of capacity >= len(self). we assume cap >= len(self)
        old = deep.copy(self._data)    # Keep track of existing list
        self._data = [None] * cap    # Allocate list with new capacity
        walk = self._head
        for k in range(self._size):    # Only consider existing elements
            self._data[k] = old[walk]    # Intentionally shift indices
            walk = (walk + 1) % len(old)    # Use old size as modulus
        self._head = 0    # Head realigned

```

Tutte le operazioni, fatta eccezione di `_resize`, sono $O(1)$ perchè realizzate con un numero costante di operazioni.

# 20. Linked lists
Le **liste concatenate** (o *linked lists*) sono strutture dati lineari in cui gli elementi non sono memorizzati in posizioni contigue di memoria, ma ogni elemento (**nodo**) contiene un riferimento al successivo (e, eventualmente, al precedente). Sono un'alternativa agli array, offrendo flessibilità nella gestione dinamica della memoria.

Ogni nodo può contenere un **dato**, cioè un valore memorizzato, oppure un **riferimento** al nodo successivo. Una lista concatenata è gestita da una classe che mantiene un riferimento al primo nodo (`head`), un rifrimento all'ultimo nodo (`tail`) e il numero di elementi (`size`).

Per accedere in ssequenza a tutti i nodi della catena, si parte dal riferimento `head` e si seguono i riferimenti contenuti nel campo *next* di ciascun nodo: si parla di *link hopping*. La scasione termina quando si trova il valore *None* nel campo *next*.

> NB: una lista concatenata è ad accesso sequeniale della memoria, mentre l'array è ad accesso casuale. Un nodo occupa più spazio di una cella di array perché contiene due riferimenti anziché uno.

Una catena vuota contiene sono un nodo `header` che ha il valore *None*; in questo tipo dilista `head` e `tail` puntano entrambi a tale `header`. Non usare il nodo di intestazione implica che i riferimenti sono uguali a *None*.

## Metodi di classe
I metodi presenti in una catena sono:
  - `addFirst`: inserire un dato all'inizio della catena.
      - Operazione di tipo $O(1)$.
      - Non c'è mai spazio inutilizzato.
  - `addLast`: inserire un dato alla fine della catena.
      - Operazione di tipo $O(1)$.
  - `removeFirst`: eliminare il primo dato.
      - Operazione di tipo $O(1)$.
  - `removeLast`: eliminare l'ultimo dato.
      - Operazione di tipo $\Theta(n)$.
  - `getFirst`: esaminare il primo dato.
  - `getLast`: esaminare l'ultimo dato.
  - `is_empty`: verificare se la catena è vuota.
  - `len`: conoscere il numero di dati contenuti nella catena.

Con questi metodi non vengono mai restituiti né ricevuti riferimenti ai nodi, ma sempre ai dati contenuti nei nodi, per questo motivo la classe **Node** è una *classe interna*. La presenza del nodo `header`, seppur "spreca" un nodo, rende più semplici i metodi della catena stessa rendendo lo spreco trascurabile per valori elevati del numero di dati. 

> Si faccia attenzione al fatto che le catene e gli array sono implementati in vari modi e sono strutture fisiche, mentre le pile e le code sono strutture dati astratte realizzate usando array o catene.

## Pila ralizzata con una catena
Entrambe le estremità di una catena hanno, prese singolarmente, il comportamento di una pila: si può realizzare una pila usando un'estremità, in particolare, è più efficiente usare l'iniio perché l operazioni sono $O(1)$.

```python
class LinkedStack:
  """LIFO Stack implementation using a singly linked list for storage."""

 #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    def __init__(self, element, next):    # Initialize node's fields
      self._element = element    # Reference to user's element
      self._next = next    # Reference to next node

 #------------------------------- stack methods -------------------------------
  def __init__(self):
	"""Create an empty stack."""
	self._head = self._Node(None, None)    # Reference to the head node
	self._size = 0    # Number of stack elements

  def __len__(self):    # Return the number of elements in the stack.
	return self._size

  def is_empty(self):    # Return True if the stack is empty.
	return self._size == 0

  def push(self, e):    # Add element e to the top of the stack
	self._head = self._Node(e, self._head)    # Create and link a new node
	self._size += 1    # Number of stack elements

  def top(self):    # Return (but do not remove) the element at the top of the stack.
	if self.is_empty():
	  raise IndexError('Stack is empty')
	return self._head._element    # Top of stack is at head of list

  def pop(self):    # Remove and return the element from the top of the stack (i.e., LIFO).
	if self.is_empty():
	  raise IndexError('Stack is empty')
	answer = self._head._element
	self._head = self._head._next    # Bypass the former top node
	self._size -= 1
	return answer

```

## Coda realizzata con una catena
Per ottenere una coda è sufficiente inserire glielementi a un'estremità della catena e rimuoverli dall'altra. Si può decidere di inserire all'inizio e rimuovere alla fine o viceversa. Affinché le operazioni siano $O(1)$, si inserisce alla fine e si rimuove all'inizio. 

```python
class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""
 #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
	def __init__(self, element, next):    # Initialize node's fields
	  self._element = element    # Reference to user's element
	  self._next = next    # Reference to next node

 #------------------------------- queue methods -------------------------------
  def __init__(self):
    """Create an empty queue"""
	self._head = self._Node(None, None)    # Reference to the head node
	self._tail = None
	self._size = 0    # Number of stack elements

  def __len__(self):    # Return the number of elements in the queue
	return self._size

  def is_empty(self):    # Return True if the queue is empty
	return self._size == 0

  def enqueue(self, e):    # Add an element to the back of queue
	newest = self._Node(e, None)    # Node will be new tail node
	if self.is_empty():
	  self._head._next = newest    # Special case: previously empty
	else:
	  self._tail._next = newest
	self._tail = newest    # Update reference to tail node
	self._size += 1

  def dequeue(self):    # Remove and return the first element of the queue (i.e., FIFO).
	if self.is_empty(): raise IndexError('Queue is empty')
	firstnode = self._head._next
	answer = firstnode._element
	self._head._next = firstnode._next
	firstnode._next = None    # Help garbage collector
	firstnode = None    # Help garbage collector
	self._size -= 1
	if self.is_empty():    # Special case as queue is empty
	  self._tail = None    # Removed head had been the tail
	return answer
```

## Coda dopppiamente concatenata
Per avere *prestazioni simmetriche*, ogni nodo deve contenere un riferimento a un dato, un riferimento al nodo successivo della lista (*next*) e un riferimento al nodo precedentedella lista (*prev*). Tutto quello che abbiamo detto per la catena (semplice) può essere esteso alla catena doppia, inoltre il metodo `removeLast` diventa $O(1)$. 

La coda doppia realizzata tramite catena doppia ha prestazioni ottimali. È uno spreco di spazio realizzare pile e code con catene doppie.

## Catena o Array?
La scelta di utilizzare catene o array è indifferente ed equialente. In una catena le operazioni sono $O(1)$, mentre nell'array `enqueue` è **mediamente** $O(1)$ e occasionalmente è $\Theta(n)$. Le catene, inoltre non permettono di accedere agli elementi usando gli indici. 






