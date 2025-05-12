first = int(input("Inserire il primo orario (es. 0930): "))
second = int(input("Inserire il secondo orario: "))
hours1 = first // 100
minutes1 = first % 100 + hours1 * 60
hours2 = second // 100
minutes2 = second % 100 + hours2 * 60
timediff = minutes2 - minutes1
"""
   La parte difficile del problema...
   quando timediff è negativo...
   si osservi che se timediff è positivo il suo
   valore NON viene modificato dall'enunciato seguente;
   quando, invece, timediff è negativo, che effetto
   ha l'enunciato seguente?
   [avete visto la novità? se ho bisogno di scrivere un commento 
    lungo, che si estende su più righe, può essere molto comodo
    usare questa diversa sintassi: si inizia con tre doppie
    virgolette e si termina con tre doppie virgolette; all'interno 
    ci può essere qualsiasi cosa tranne... tre doppie virgolette!]
"""
timediff = (timediff + (60*24)) % (60*24)
hours = timediff // 60
minutes = timediff % 60
print("Tempo trascorso:", hours, "ore e", minutes, "minuti")
"""
   Come si comporta il programma nel caso in cui i due orari siano identici?
   Avevate previsto questo caso durante il collaudo?
   E durante la progettazione? 
   Che ipotesi avete fatto?
   E' meglio visualizzare che il tempo trascorso tra
   i due orari è zero oppure 24 ore?
   In mancanza di specifiche piu' precise, entrambe le scelte sono ragionevoli:
   meglio scrivere in un commento quale
   scelta è stata adottata durante la progettazione.
"""