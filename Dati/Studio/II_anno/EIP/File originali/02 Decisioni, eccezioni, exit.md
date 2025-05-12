02 Decisioni, eccezioni, exit

# 2. Decisioni, eccezioni, exit

#### Tabulazioni
Python richiede come tabulazione 4 spazi. Più o di meno e da errore.


## *Operatori relazionali*
|Operatori|Funzione|
|:---:|---|
|<|minore di|
|>|maggiore|
|<=|minore o uguale|
|>=|maggiore o uguale|
|!=|diverso|
|==|uguale|

L'operatore = viene usato solo per assegnare, non per confrontare.

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
#### Assegnazione condizionale
```python
variabile = 2 if x>0 else 3
```
#### Assegnazione condizionale 2
```python
actualFloor= floor-1 if floor > 3 else floor

#che e' equivalente a:
if floor>13:
  actualFloor=floor-1
elif floor=13:
	dp=3
else:
  actualFloor=floor
```
  
## *Eccezioni - Try/Except*

#### Codice che da eccezione:
```python
astr="Una stringa qualsiasi"
istr=int(astr)
```
#### Correzione usando _try/except_:

```python
try: #prova a fare questo
	istr=int(astr)
except: #se ti da eccezione, errori, ecc, esegui questo
	istr=-1
```
Cerca sempre di minimizzare il codice all'interno del try per ottimizzare il codice.


___
## *Eccezioni - Try/Except*

#### Codice che da eccezione:
```python
astr="Una stringa qualsiasi"
istr=int(astr)
```
#### Correzione usando _try/except_:

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
#E' definita nel modulo sys della libreria standard'

exit("Error, you did some stupid shit so i exited the program.") 
#termina l'esecuzione del programma con un messaggio.'
```