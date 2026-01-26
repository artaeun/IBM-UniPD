03 Condizionali While

# 3. Condizionali

## *Ciclo WHILE*

#### Forma base
```python
while booleanConditionTrue:
    # do whatever
    pass
```

Il ciclo finisce quando la condizione booleana diventa falsa. Altrimenti si finisce in un loop infinito.
```python
while True:
    line = input()
    if line[0] == '#':
        continue  # continua
    if line == 'done':
        break  # rompe il ciclo while
    print(line)
print('Done')
# questo codice stamperà man mano ogni riga scritta,
# e si fermerà solo quando gli inviamo 'done'
```
___
## *Ciclo FOR*

#### Forma base:
```python
for i in [5, 4, 3, 2, 1]:
    print(i)  # prints: 5, 4, 3, 2, 1
print('Blastoff!') 
```
#### Un'altra forma:
```python
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year', friend)  # Happy New Year Joseph, ecc.
print('Done!')
```
#### La funzione _range()_:
```python
for i in range(1, 10):
    print(i)
```
che equivale a:
```python
i = 1
while i < 10:
    print(i)
    i = i + 1
```

La funzione _range(n, m)_ genera numeri interi nel range proposto tra _n_ ed _m-1_. Es.: range(1, 4) => 1, 2, 3. Utile principalmente con il ciclo _for_.

#### Altro modo per usare _range()_:

```python
for i in range(5):
    # do something (i va da 0 a 4)
    pass
```
equivalente a:
```python
for i in range(0, 5):
    # do something
    pass
```

Altro esempio con _range_ ma usando un valore incrementale:
```python
for i in range(1, 11, 2):
    # do whatever (i = 1, 3, 5, 7, 9)
    pass
  
# il terzo valore è l'incremento del range. Es:
# 1, 1+2=3, 3+2=5, ecc.
```
___
## *Funzioni per numeri casuali*
```python
from random import *

random()      # ritorna un numero casuale tra 0 e 1
randint(a, b) # ritorna un numero casuale intero tra a e b (inclusi)
```

## *Metodo Monte Carlo*

Trova soluzioni approssimate a problemi i cui risultati non possono essere precisi. Per esempio, per calcolare PiGreco.

Metodo:
1. Simuli il lancio di una freccetta all'interno di un quadrato circoscritto a un cerchio di raggio 1 e centro (0, 0)
2. Basta generare valori casuali tra -1 e 1 per x e y
3. Se il punto generato è dentro al cerchio, allora il bersaglio è "colpito": questo accade se x² + y² ≤ 1
4. Dato che i lanci sono casuali, ci aspettiamo che hits/tries sia circa uguale al rapporto tra le aree del cerchio e del quadrato, cioè π/4
5. La stima del nostro valore di π è uguale a: 4 × hits/tries
___

## *IS / IS NOT*

#### Uso delle funzioni:

Fai qualcosa se la variabile non ha mai ricevuto valore:
```python
if smallest is None:
    # do something
    pass
```

Fai qualcosa se la variabile ha un qualsiasi valore:
```python
if smallest is not None:
    # do something
    pass
```
Non puoi usare _==None_ o _!=None_ per confrontare con questo valore speciale. Usa sempre _is None_ o _is not None_. 
