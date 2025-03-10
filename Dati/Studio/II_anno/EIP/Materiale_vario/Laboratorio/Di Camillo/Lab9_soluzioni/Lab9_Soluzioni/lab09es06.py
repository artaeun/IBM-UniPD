## Scrivere un programma che legga il file sample_mbox.txt 
## e indichi quanti messaggi vengono ricevuti nelle diverse ore
## (senza considerare i minuti quindi) del giorno.
## Il programma cerca le righe che cominciano con ‘From’ (non 'From:'')
## e crea un dizionario che memorizza le ore
## e quante volte sono apparse.
## Una volta che il dizionario è stato creato, ordinare in base alle ore
## e utilizzare un ciclo for per stampare il numero di messaggi ricevuti per i diversi orari

fname = input("Enter file name: ")
fh = open(fname,encoding="latin1")
counts = dict()

for line in fh:
   if not line.startswith("From"): continue
   if line.startswith("From:"): continue
   ora_completa = line.split()[5]
   ora= ora_completa.split(":")[0]
   counts[ora] = counts.get(ora,0) + 1

ore_ordinate=sorted(counts.items())
for k, v in ore_ordinate:
   print(k, v)