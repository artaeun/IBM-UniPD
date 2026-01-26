01 Variabili e operazioni

# 1. Variabili e operazioni



## *Variabili*
Nomi permessi delle variabili → nomi che iniziano con una lettera o un underscore. I caratteri successivi devono essere cifre, lettere o underscores. È case sensitive.

#### Assegnazione:
```python
x=12 #intero
y=1.2 #float
z="Ciao" #string
```

#### Conversione di tipo:
```python
y = int(x)   # converte x in un intero e salva in y
y = float(x) # converte x in un float, variabile a virgola mobile
y = str(x)   # converte x in una stringa e salva in y
```

#### Altre funzioni:
```python
# === Tipo dato ===
type(x)  # ci ritorna il tipo della variabile x

# === Lunghezza stringa ===
length = len("World!") #length ha valore 6

# === Concatenazione ===
firstName = "Harry"
lastName = "Potter"
fullName = firstName + " " + lastName 
# fullName = "Harry Potter"

# === Sottostringhe ===
print(firstName[0])
# ritorna "H"
print(firstName[len(firstName)-1])
# ritorna "y"
print(firstName[0:3])
# ritorna "Har"
print(firstName[:3])
# ritorna "Har"
print(firstName[3:])
# ritorna "ry"
print(firstName[:])
# ritorna "Harry"

# === Ripetizione stringa ===
stringa = "x"
print(stringa * 3)
# ritorna "xxx"
``` 

___
## *Operazioni*

#### Operatori aritmetici:
```python
z = x + y  # addizione
z = x - y  # sottrazione
z = x * y  # moltiplicazione
z = x / y  # divisione
z = x ** y # elevamento a potenza y
z = x // y # divisione intera (risultato è l'intero)
z = x % y  # resto della divisione intera (modulo)
``` 
#### Algoritmo confronto tra numeri di tipo float:

```python
from math import sqrt
EPSILON = 1E-14
r = sqrt(2.0)
if abs(r * r - 2.0) < EPSILON:
    print("sqrt(2.0) squared is approximately 2.0")
```
#### Modulo math di Python:

Basta importarlo per usare le funzioni varie offerte.

```python
from math import *  # o per ottimizzare si può fare
from math import sqrt

y = sqrt(x)       # radice quadrata
y = trunc(x)      # tronca il valore in intero
y = cos(x)        # coseno di x in radianti
y = sin(x)        # sin(x) in radianti
y = tan(x)        # tan di x in radianti
y = exp(x)        # e^x
y = degrees(x)    # x da radianti in gradi
y = radians(x)    # x da gradi in radianti
y = log(x)        # log x in base e
y = log(x, base)  # log x in base indicata

# in alternativa:
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
name = input("Chi sei?")  # stampa "Chi sei?", e riceve input
# input è SEMPRE una stringa
print(name)  # stampa il nome ricevuto in input
```
