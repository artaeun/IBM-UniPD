##Scrivete un programma che legga i numeri inseriti uno a uno dall’utente fino a che l’utente non inserisce la parola chiave 'fine'.
##Il programma, una volta che l’utente ha inserito 'fine', stampa a monitor, la somma e la media dei numeri inseriti.
##
##Esempio di esecuzione:
##>inserisci un numero o la parola fine: 4
##>inserisci un numero o la parola fine: 5
##>inserisci un numero o la parola fine: 7
##>inserisci un numero o la parola fine: fine
##somma= 16 
##media= 5.333333333333333

count = 0
somma = 0
while True:
    input_str = input ("inserisci un numero o la parola fine: ")
    if input_str == "fine":
        break
    else:
        value = float(input_str)
        count = count + 1
        somma = somma + value
if (count>0):
    media = somma / count
else:
    media = None
print('somma=', somma, " media=", media)

