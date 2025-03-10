03 Condizionali While

# 3. Condizionali

## *Ciclo WHILE*

#### Forma base
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
	if line=='done'
		break #rompe il ciclo while
	print (line)
print('Done')
#questo codice stamperà mano a mano ogni riga scritta,
#e si fermera' solo quando gli inviamo 'done'
```
___
## *Ciclo FOR*

#### Forma base:
```python
for i in [5,4,3,2,1]:
	print(i) #prints: 5,4,3,2,1,Blastoff!
print('Blastoff!') 
```
#### Un'altra forma:
```python
friends = ['Joseph', 'Glenn', 'Sally']
for friends in friends:
	print('Happy New Year', friends)#Happy New Year: Joseph, ecc.
print('Done!')
```
#### La funzione _range()_:
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

#### Altro modo per usare _range()_:

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
3. dato che i lanci sono casuali, ci aspettiamo che i hits/tries sia circa uguale al rapproto tra le aree del cerchio e del quadrato, cioe' pi/4
4. la stima del nostro valore di pi e' uguale a: 4*hits/tries
___

## *IS / IS NOT*

#### Uso delle funzioni:

Fai qualcosa se la variabile non ha mai ricevuto valore:
```python
if smallest is None: #do something
```

Fai qualcosa se la variabile ha un qualsiasi valore. 
```python
if smallest is not None: #do something
```
Non puoi usare _non==None_ o _!=None_ per usare questo valore speciale. 
