##    Un biologo ha bisogno di un programma per prevedere la crescita di una popolazione di batteri
##    in un certo intervallo di tempo di osservazione.
##    Gli input sono:
##        - il numero iniziale di organismi
##        - il tasso di crescita all'ora in percentuale
##        - l'intervallo (in ore) di osservazione
##    Supponendo che nessun organismo muoia si scriva un programma che accetti questi input
##    e visualizzi una previsione del numero totale di batteri alla fine dell'intevallo di osservazione

##    Esempio di esecuzione
##    numero iniziale di organismi: 5
##    tasso di crescita all'ora in %: 2
##    intervallo (in ore) di osservazione: 24
##    il numero di batteri dopo 24.0 ore è uguale a 5



numBatteri = int(input("numero iniziale di organismi: "))
rate_crescita = float(input("tasso di crescita all'ora in %: "))
intervallo = int(input("intervallo (in ore) di osservazione: "))

tempo = 0
while (tempo < intervallo):
    tempo = tempo + 1
    numBatteri = numBatteri + round(numBatteri*rate_crescita/100)

print("il numero di batteri dopo", intervallo, "ore è uguale a", numBatteri)
