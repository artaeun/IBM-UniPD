## Scrivere, usando una o più funzioni, un programma che legga
## un file con la struttura del file sample_mbox.txt 
## e trovi chi ha scritto il maggior numero di messaggi.
## Il programma cerca le righe che cominciano con ‘From:’
## e crea un dizionario che memorizza gli indirizzi dei mittenti 
## racchiusi tra i simboli < > e quante volte sono apparsi nel file.
## Una volta che il dizionario è stato creato, il programma lo legge
## e trova il mittente che ha inviato il maggior numero di email.

import re

def dizionarioemail():
   fname = input("Enter file name: ")
   fh = open(fname,encoding="latin1")
   counts = dict()
   for line in fh:
      y = re.findall('^From: .*<(\S+@\S+)>',line)
      if len(y)>0:
         email_address=y[0]
         counts[email_address] = counts.get(email_address,0) + 1

##   for k,i in counts.items():
##      print (k,i)
   G=greaterfreq(counts)
   return G
   
def greaterfreq (dizionariocounts):
   bigcount = None
   bigaddress = None
   for email,count in dizionariocounts.items():
    if bigcount is None or count > bigcount:
        bigaddress = email
        bigcount = count
   return(bigaddress, bigcount)

piu_frequente=dizionarioemail()
print(piu_frequente)