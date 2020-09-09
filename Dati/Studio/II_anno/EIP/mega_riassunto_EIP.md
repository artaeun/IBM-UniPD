programma INFORMATICA
- Il linguaggio di programmazione Python: 
    - tipi di dati elementari
        - tipi:
            - int (intero)
            - float (a virgola mobile)
            - string (stringa di testo)
        - cast:  
            es: float(x) #converte x in un float, variabile a virgola mobile
    - numeri e stringhe
        - numeri:
            operazioni: + - * / 
                        ** - potenza
                        // - divisione con risultato intero
                        %  - solo resto divisione intera
        - stringhe:
            - firstName[0,3] = tutto tra il primo carattere e il 4o (escluso)
            - firstName[:3] = tutto fino al 4o escluso
            - "n" in variabileStringa = da True o False in base al fatto che abbia trovato o meno la sottostringa relativa.
            - x > y = confronto lessicografico, da boolean. 
                Maiuscole < Minuscole
                Spazio < Qualsiasi altra cosa
                Numeri < caratteri

            - funzioni importanti:
                - ```>>> len(stringa)```  = nr caratteri in stringa
                - ```>>> .upper() / .lower()``` = tutti i caratteri della stringa maiuscoli / minuscoli
                - ```>>> .isupper() / .islower()``` = ritorna True o False se la stringa è maiuscola / minuscolo
                - ```>>> .find(sottostringaDaCercare)``` = cerca nella stringa la sottostringa, restituisce l'indice corrispondente, altrimenti restituisce -1. E' case sensitive
                - ```>>> .replace(sottStrinDaSostituire, sottStrinConCuiSostituire)```= cerca stringa & sostituisce
                - ```>>> .lstrip() / .rstrip() / .strip()``` = rimuove spazi a sx/dx/sia a sx che dx
                - ```>>> .startswith(sottostringa)``` = restituisceBoolean se la stringa da analizzare inizia con la sottostringa
                - ```>>> print("%.2f" % price)``` = restituisce il valore di price con 2 cifre decimali.
                    - - ``` %d``` = interi
                    - - ``` %f``` = virgola mobile
                    - - ``` %s``` = stringhe
                - ```>>> .isalpha()``` = true false se è alfa 
                - ```>>> print("%d, %10.2f" % (quantity, total))``` = uso più esteso dell'operatore di formato
                - ```>>> string.split(carattereDelimitazione)``` =crea lista di stringhe usando il carattereDelimitazione. Se non specificato, spazi successivi vengono trattati come uno solo


    - espressioni e operatori
        - modulo math - from math import *
            - ```sqrt``` - square root
            - ```abs``` - absolute
            - ```trunc``` - tronca il valore in intero
            - ```exp``` - e^x
            - ```log(x)``` - logaritmo natural
            - ```round(x)``` - arrotonda

        - modulo random -
            - ``` random()``` - nr casuale tra 0 e 1
            - ```randint(a,b)``` - nr casuale tra a e b

        - espressioni regolari (regex):
            ```python
            ^	#Matches the beginning of a line
            $	#Matches the end of the line
            .	#Matches any character
            \s	#Matches whitespace
            \S	#Matches any non-whitespace character
            \d	#Matches digit
            \D	#Matches any non-digit character
            *	#Repeats a character zero or more times
            *?	#Repeats a character zero or more times (non-greedy)
            +	#Repeats a character one or more times
            +?	#Repeats a character one or more times (non-greedy)
            [aeiou]	#Matches a single character in the listed set
            [^XYZ]  #Matches a single character not in the listed set
            [a-z0-9]#The set of characters can include a range
            (	    #Indicates where string extraction is to start
            ```
            
            ```python
            #per importare e fare una ricerca in una stringa
            >>> import re
            >>> re.search(sottostringaDaCercare,stringaInCuiCercare)#sottostringaDaCercare corrisponde a espressione in re
            >>> re.findall(sottostringaDaCercare,stringaInCuiCercare)
            #########ESEMPIO#########
            >>> stringa = "Peter Pan"

            >>> print(re.findall("[aeiou]",stringa))
            ['e', 'e', 'a']

            >>> print(re.findall("[\S]",stringa))
            ['P', 'e', 't', 'e', 'r', 'P', 'a', 'n']

            >>> print(re.findall("[^XYZ]",stringa))
            ['P', 'e', 't', 'e', 'r', ' ', 'P', 'a', 'n']
            ```


    - istruzioni di controllo
        - operazioni relazionali (danno un boolean):
            ```
            >
            <
            <=
            >=
            !=
            ==
            ```
        - operatori logici:
            ```
            and
            or
            not
            ```
        - condizionali:
  
            ```python
            >>> if(this):
                #do this
            else if(this):
                #do this
            else:
                #do this
            ```

            ```python
            >>> while(condizione):
                #do this
                if (something):
                    break #interrompi completamente la iterazione
                if (somethingElse):
                    continue #interrompi questa iterazione e riprendi dalla prossima
            ```

            ```python
            >>> for i in range(x,y):
                #do stuff
            ```

    - funzioni
        ```python
        >>> exit()- esce da software - from sys import exit
        >>> is/is not - confrontare una variabile con "None". Se non ha mai ricevuto un valore è "None".
        >>> range(a,b) - usato per i for
        ```
    - eccezioni
        ```python
        >>> try: #prova a fare questo
        >>>     istr=int(astr) #esempio conversione in int
        >>> except: #se ti da eccezione, errori, ecc, esegui questo
        >>>     istr=-1 #se "astr" è stringa, il valore impostato è -1
        ```

    - operazioni di ingresso e uscita da file di testo
        - aprire file in lettura:
            ```python
            >>>file = open("input.txt","r")
            ```
        - aprire in scrittura:    
            ```python
            >>>file = open("input.txt","w")
            ```
        - scrivere nel file:  
            ```python
            >>>file.write("Stringa")
            ```
        - terminare elaborazione:  
            ```python
            >>>file.close()
            ```
        - tutto un file in una stringa:
            ```python
            >>> stringaFile=file.read()
            >>> print(len(inp))
            ```
        - una riga alla volta in stringa:
            ```python
            >>>line=file.readline()
            ```
        - leggere parole:
            ```python
            >>> etc = line.split() # crea una lista #```
            >>> etc = line.split(";") # ; come separatore #
            ```
        - prendere nomefile come argomento in riga di commando:
            ```python
            >>> from sys import argv
                file = open(argv[1],"w")
            ```
            ```python
            >>> script.py nomefile.txt #da console#
                # argv sempre lista con path del SourceCode in pos 0  
            ```

    - liste
        ```python
        >>> lista[indiceElemento] #ritorna la lista
        >>> lista[1:3] #sottolista con 2 elementi
        >>> len(lista) #elementi in lista
        >>> lista1==lista2 #confronto dei valori di due liste
        >>> lista1 is lista2 #verifica se lista1 è un riferimento di lista2
        >>> lista2=list(lista1) #copia intera (e non riferimento) di una lista
        >>> lista1+lista2 #crea una terza lista che contiene gli elementi di tutte e due le liste
        
        >>> max(listaNumeri) #ritorna il valore massimo
        >>> min(listaNumeri)
        >>> sum(listaNumeri) #somma di tutti i valori, media si fa usando len

        >>> lista.append(item) #aggiunge l'elemento alla lista (in fondo)
        >>> lista.insert(indice,item) #aggiunge a indice l'elemento, spostando tutti quelli dopo in avanti di indice.
        >>> lista.pop() #rimuove l'ultimo valore della lista e lo restituisce per uso
        >>> lista.pop(indice) #rimuove dalla lista l'elemento all'indice e sposta tutti gli altri valori per riempire il buco creatosi. Restituisce il valore per uso.
        >>> lista.remove(item) #rimuove l'elemento dalla lista. Bisogna verificarne l'esistenza prima per evitare eccezioni

        >>> lista.index(item) #cerca elemento e restituisce il suo indice dentro la lista. Può creare eccezione
        >>> item in lista #da True o False dopo la ricerca

        >>> lista.sort() #ordina lista (ordine numerico o lessicografico)
        ```

    - insiemi
        - tuple
            - non possiamo modificare il contenuto di una tupla una volta creata. Per il resto sono come liste.
            - sono più efficienti di una lista.

                ```
                >>> x=(1,3,2) -  esempio creazione tupla
                >>> (x,y)=(2,3) - altro esempio assegnazione di tupla. Così assegno a x 2, e a y 3

                >>> tupla.count()
                >>> tupla.index()
                ```
            - confronti: 
                ```python
                >>> (0,1,2) < (5,1,2) #da "True"
                #confronto tra il primo elemento della prima tupla e il primo della seconda. Se il primo è false, passa al confronto tra i secondi,ecc. Poi fa OR di tutti i risultati#
                ```

    - grafica
        - ezgraphics
            ```python
            #import
            >>> from ezgraphics import GraphicsWindows
            >>> win = GraphicsWindows() #creata nuova finestra di default 400 x 400
            >>> canvas=win.canvas()

            >>> canvas.drawRect(x=5,y=10,width=20,height=30) #disegna rettangolo in punto x y con larghezza e altezza

            >>> canvas.drawLine(x1,y1,x2,y2)
            >>> canvas.drawOval(x,y,width,height)

            >>> win.wait() #per evitare la terminazione immediata della finestra grafica.

            >>> canvas.setOutline(redHex,greenHex,blueHex) #imposto il colore per disegnare
            >>> canvas.setOutline(colorname) #uso un nome comune in inglese per il colore.

            >>> canvas.setFill(red, green, blue)
            >>> canvas.setFill(colorname)

            >>> canvas.drawText(50, 100, ‘Rettangolo’)
            ```

        - tkinter
            ```python
            >>> import tkinter
            >>> pannello = tkinter.Canvas()
            >>> pannello = tkinter.Canvas(width=500,height=400,bg='cyan')
            >>> pannello.pack()

            >>> pannello.create_oval(1, 1, 50, 50)
            >>> pannello.create_line(1, 1, 50, 50)
            >>> pannello.create_rectangle(1, 1, 50, 50)
            
            >>> canvas.create_text(80, 90, text='PC')

            >>> pannello.mainloop() # ferma la finestra dalla terminazione immediata
            ```

            - GIF
                ```python
                >>> gif1 = PhotoImage(file = 'DECK\\10c.gif')
                >>> gif2 = PhotoImage(file = 'DECK\\1d.gif‘)

                # put gif image on canvas
                >>> canvas.create_image(80, 100, image = gif1, anchor = NW)
                >>> canvas.create_image(250, 100, image = gif2, anchor = NW)

                #put some text
                >>> canvas.create_text(80, 90, text='PC')
                >>> canvas.create_text(250, 90, text='Me')
                ```

- Istruzioni utili:
    ```python
    type(variabile) #=> restituisce il tipo della variabile
    dir(oggetto) #=> funzioni/metodi disponibili per l'oggetto
    ord(carattereStringa) #=> restituisce il codice unicode del carattere
    chr(nrCarattere) #=> restituisce il carattere corrispondente al codice unicode.
    ```
    - ***Dizionari***
        - proprietà:
            - ogni chiave è unica
            - valori non devono essere per forza univoci
        - in Python:
            ```python
            #dichiarazione:
                >>> borsa = dict()
                    o in alternativa
                >>> borsa = {}
            #copiare dizionari:
                >>> copiaDizionario=dict(dizionarioOriginale)
            #aggiungere elementi:
                >>> borsa[chiave]=valore
                    # chiave e valore sono tipi di dati qualsiasi    
            #usare gli elementi:
                >>> borsa[chiave]=nuovoValore
            #eliminare elementi:
                >>> borsa.pop(chiave)
            #iterare su un dizionario:
                >>> for key in contatti:
                        print(key)
                        print(contatti[key])
            #cercare/verificare presenza chiave in dizionario:
                >>> if (chiaveEsempio in dizionarioEsempio):
                        # fai quello che ti serve
            #cercare con default:
                >>> dizionarioEsempio.get(chiaveRicerca, valoreDefault)
                # valoreDefault viene restituito se la chiave non viene trovata #
                # utile per contare in modo furbo le ripetizioni di un determinato 
                #valore in una lista e salvarlo in un dict #
            
            #iterare su due valori al contempo:
                >>> jjj = {...}
                    for (a,b) in jjj.items():
                        print(a,b)
            #recuperare lista sole chiavi di un dizionario:
                >>> listaChiavi=jjj.keys()
            #recuperare lista soli valori:
                >>> listaValori=jjj.values()
            #recuperare chiavi e valori in lista di tuple:
                >>> listaTuple = jjj.items()
            #ordinare rispetto a chiavi:
                # uso items per avere la lista di tuple, poi uso sorted():
                >>> sorted(d.items()) #lista tuple ordinate secondo chiave
            #ordinare rispetto a value:
                >>> for k, v in dicti.items():
                        tmp.append( (v,k) )
                        tmp=sorted(tmp)
            ```

    - oggetti e classi (da slide)
    - ereditarietà (da slide)
    - operazioni di ingresso e uscita dall'ingresso e dall'uscita standard (da slide) 


    - strutture dati
        - pile
            - solo punto di accesso per inserire e reperire i dati
            - come un tubo lungo e verticale, i dati (come dei piatti) possono essere inseriti dalla cima ed estratti sempre dalla cima
            - la pila (stack) può seguire un comportamento del tipo "Last in, First Out", in cui l'ultimo oggetto inserito è il primo ad essere rimosso (es meccanismo: CTRL+Z dei PC)
            - l'unico oggetto ispezionabile è quello che verrebbe rimosso => non c'è modo ispezionare la pila senza svuotarla ordinatamente (accesso sequenziale distruttivo)
            - metodi disponibili:
                - push = inserisce un dato in cima
                - pop = restituisce l'ultimo elemento rimuovendolo (non invocabili con pila vuota)
                - top = ispeziona l'ultimo elemento (non invocabile con pila vuota)
                - is_empty = verifica se è vuoto il contenitore
                - len = fa sapere il numero di elementi dentro i contenitori
            - prestazioni migliori O(1), prestazioni peggiori O(n)
        - code
            - chiamate anche "queue"
            - "First in First Out", molto come un verme che mangia delle palline. Prima e entrare dalla bocca è la prima a essere digerita e mandata fuori.
            - l'unico oggetto ispezionabile è il primo della coda, quindi anche qui non è possibile visualizzare l'intera coda senza svuotarla ordinatamente
            - Operazioni:
                - enqueue = per inserire un dato alla fine della coda
                - dequeue = per eliminare il dato che si trova all'inizio della coda, restituendolo al chiamante
                - Front / getFront = ispeziona il dato all'inizio della coda senza estrarlo
                - is_empty = verifica se è vuoto il contenitore
                - Size/len = fa sapere il numero di elementi dentro i contenitori
            - realizzazione:una lista con elementi di cui aggiungo elementi e faccio pop in indice 0.
            - prestazioni O(n)
            - ci sono code ad implementazione circolare, nel quale viene semplicemente tenuto conto della posizione dell'ultimo elemento che viene eliminato, e così facendo non serve traslare ogni elemento della coda di 1. 
                - Questa è una struttura logica che però fisicamente è un semplice array di dati.
                - servono due indici, per "Head" e "Tail"
                - ovviamente head non deve superare tail e viceversa. 

- CPU
    -  La cpu ha vari registri, tra cui i più importanti:
        - registro IR (IP) - Instruction Register <= istruzione correntemente in esecuzione. La CPU la legge ed esegue
        - registro PC (P) - Program Counter <= indirizzo in memoria centrale della prossima istruzione da eseguire. Viene modificato a ogni istruzione per contenere l'indirizzo dell'istruzione successiva.
        - registro RC - registro che contiene il risultato di un confronto.
        - R0 ... R7 - dati
    - Tipi di operazioni:
        - trasferimento di dati tra RAM e registri Rn
            - LOAD nrRegistro indirizzoRam
            - STORE nrRegistro indirizzoRam
        - trasferimento di dati tra Ram e dispositivi Input/Output
            - READ indirizzoDispIO indirizzoRam
            - WRITE indirizzoDispIO indirizzoRam
        - operazioni aritmetiche (somma, differenza, moltiplicazione e divisione)
            - tra interi (segue "reg***I***" di Imola, J di Jesolo)
                - ADD regI regJ 
                - SUB regI regJ
                - MULT regI regJ
                - DIV regI regJ
                - MOD regI regJ
            - tra reali
                - FADD regI regJ
                - FSUB regI regJ
                - FMULT regI regJ
                - FDIV  regI regJ
        - operazioni di controllo (confronto, salto, stop)
            - confronto
                - COMP regI regJ - se Ri < Rj, salva -1. Se uguali 0, se Ri>Rj 1. salva risultato in RC
                - FCOMP regI regJ
            - salto (branch). Confronta con il valore di RC (cioè a seguito di un confronto). Se verificata la condizione salta a indirizzo RAM
                - BREQ indirizzoRam - branch if equal
                - BRGT indirizzoRam - branch if greater than
                - BRLT indirizzoRam - branch if lower than
                - BRGE indirizzoRam - branch if greater or equal
                - BRLE indirizzoRam - branch if lower or equal
                - BRNE indirizzoRam - branch if not equal
            - stop

- Organizzazione di un elaboratore: unità centrale di elaborazione, memoria centrale, memoria di massa, dispositivi di ingresso e uscita.

    - Il primo strumento di calcolo utilizzato nell'antichità da Greci e Romani fu l'abaco.

    - Blaise Pascal (1623-1662, francese) costruì una macchina (a soli 19 anni) che eseguiva - solo somme e sottrazioni e che utilizzava le dieci cifre decimali → la "Pascalina"

    - Leibnitz ideò il sistema numerico binario.

    - Charles Babbage ideò una macchina, detta “alle differenze”, con la quale si potevano costruire tavole astronomiche e una, detta “analitica” (mai costruita), alla quale si dovevano fornire schede perforate contenenti sia i dati da elaborare che le regole (istruzioni) di calcolo da eseguire.

    - Ada Augusta Byron fu la prima programmatrice della storia. Linguaggio Ada (1979) è nominato così in suo onore. Ella scrisse una sequenza di istruzioni (programma) per la macchina di Babbage, con le quali si calcolavano numeri di Bernoulli.

    - La macchina a schede perforate, dello statunitense Hermann Hollerit fu la prima ad usare elettricità (1890).

    - John Von Neumann elaboro un modello teorico dell'architettura di un elaboratore che è tuttora valido e molto utilizzato (eccezioni sono le macchine ad elaborazione parallela). Nell'architettura di Von Neumann la memoria principale della macchina è condivisa dai dati e dai programmi. Nell'architettura Harvard invece esiste una memoria separata per i dati ed una per i programmi.

        - il modello suddivide il computer in CPU, Memoria Principale (RAM, ROM), Secondaria(HD, CD, DVD, ecc), Dispositivi I/O, tutti legati insieme dal bus dati.
        = CPU = La CPU esegue codice scritto in linguaggio macchina, ripetendo continuamente una serie di cicli ADE (Access=legge l'istruzione da eseguire dalla RAM, Decode = riconosce di quale istruzione tra le possibili si tratta, Execute = la esegue) o FDE (Fetch, Decode, Execute). Un ciclo completo è "Accesso, Decodifica, Esecuzione, Memory, Write-Back".
          - la ADE ha come fasi opzionali l'attivazione della memoria e la scrittura del risultato in un registro opportuno (quindi due fasi aggiunte in più).
        - CPU composta da tre parti principali:
            - ALU (Arithmetic Logic Unit)
            - Unità di controllo (ne governa il funzionamento)
            - registri (spazi di accesso molto veloce)
        - Architetture sulla base delle istruction set:
            - CISC (Complex Instruction Set Computer) - i7, transistor budget usato per massimizzare la taglia delle istruction set
                - Minore dimensione del codice, complessità spostata sul hardware
                - ampio insieme di istruzioni che permettono di compiere operazioni semplice e anche complesse. 
            - RISC (Reduced INstruction Set Computer) - Power PC della IBM, transistor budget usato per velocizzare un repertorio limitato di istruzioni (load/store)
                - complessità spostata al software, quindi più codice
                - insieme di funzioni base,  mono-ciclo 
           - CPU funziona in modo ciclico (clock)
             - a ogni ciclo di clock viene eseguita una fase (circuito specializzato) del ADE. Quindi ci vogliono cinque cicli di clock per fare un ciclo ADE intero (con opzionali) 
                - usando le pipeline posso incrementare il *throughput* (quantità di istruzioni eseguite in una data quantità di tempo) parallelizzando i flussi di elaborazione di più istruzioni. Quindi il primo ciclo ADE può essere si eseguito in cinque cicli di clock. Ma il successivo termina dopo un altro ciclo di clock, e quello dopo ancora dopo un altro e così via. Perché tenendo attivo un circuito solo per il Fetch, l'altro per il Decode, ecc, questi possono continuare ad eseguire il prossimo lavoro senza aspettare che finisca tutto il ciclo ADE
        = MEMORIA PRIMARIA = veloce ma costosa. Composta di chip in silicone, divisa tra ROM (READ ONLY MEMORY) e RAM (RANDOM ACCESS MEMORY).
        - ROM è scritta una volta sola, poi solo letta, e dunque molto veloce per rileggere alcuni pezzi di codice elementari. Tipi di ROM sono le PROM, EPROM, EEPROM, FLASH. Non si perde con lo spegnimento del computer. 
        - RAM è suddivisa in bit < byte < parole di 32 bit (che sono un aggregato di byte). In 2D, un bit è una cella di una riga. Un byte una riga intera. Una parola una tabella di più righe.
                - 1 byte = 8 bit. 
          - CACHE - tipo particolare di RAM, molto vicina alla CPU, e di facile comunicazione. (cache = tesoro, nascondiglio, munizioni). Si mette da tramite tra RAM e CPU per non rallentare i tempi di esecuzioni delle istruzioni, e fa un po' da tampone. Ma NON FA PARTE DELLA CPU. Quelle più specializzate fanno anche una predizione sulla prossima istruzione da eseguire, velocizzando ulteriormente le operazioni. Viene anche usata per ridurre il traffico sul BUS di sistema.
        - BIOS (Basic INPUT OUTPUT SYSTEM) - serve per eseguire test diagnostici per controllare il funzionamento del hardware e segnalare eventuali guasti, localizzare il OS e caricarlo nella RAM, fornire un'interfaccia software per l'accesso alle periferiche e al hardware del PC. Gli OS più moderni non usano il BIOS per il I/O ma accedono direttamente al Hardware.
                - il caricamento in RAM del SO si chiama "bootstrap"
        = MEMORIA SECONDARIA = tempo di accesso di un settore determinato da Seek+Latency+Transmission. Dischi sono affidabili, ma in modo limitato. Per quello va introdotta ridondanza per rilevare errori e correggerli. Gku SSD sono molto più veloci e non usano componenti meccanici, ma sono circa 10 volte più costosi del HDD.
            
        - Gerarchia di memoria sulla base di costo/velocità: Registri>Cache L1> Cache L2> RAM > Dischi
        = I/O = ogni tipo di dispositivo periferico, inclusi schermi, altoparlanti, perfino connessione di rete e touchscreen (che sono bidirezionali)
        = BUS = secondo il modello di Von Neumann è costituito da tre bus distinti:
                  - bus dei dati (da e a CPU)
                  - bus degli indirizzo (da CPU)
                  - bus dei segnali di controllo (da CPU)

      - Tutto il BUS è nella scheda madre, la quale si occupa anche di temporizzazione dei segnali.
    
    - Dagli anni 40 in poi i calcolatori sono diventati macchine universali (che realizzano dunque applicazioni diverse/più di una). Così si distinguono diverse generazioni di macchine:
        - Gen 1 ('40-'50):
            - EDVAC e lo IAS progettati da J. Von Neumann
            - ENIAC, a valcole termoioniche (tubi a vuoto)
            - UNIVAC
            - IBM 701
        - Gen 2 ('50-'60), con i transistor e primi linguaggi ad alto livello e primi OS:
          - Fortran
          - Circuiti integrati
          - IBM 7090
          - Mouse
        - Gen 3 ('60-'70), uso massivo di IC, con la realizzazione dei primi Chip
          - Intel 4004
          - ARPANET
          - ETHERNET
          - IBM 5100, Commondore Pet
          - IBM PC
          - Apple Macintosh
        - Gen 4 (attuale)
            - Very Large Scale Integration (VLSI)
            - Ultra Large Scale Integration (ULSI) - milioni di transistor
        - Gen 5 (attuale)
            - Wafer Scale Integration - centinaia di milioni di transistor

- Il sistema operativo: sommario delle funzioni, processi, multitasking.
    - I componenti di un PC sono composte di porte logiche (AND, OR, NOT). Con questi vengono creati nuovi circuiti molto più complessi.
    - Si possono eseguire operazioni elementari (somma, moltiplicazione, ecc) con rischio però di overflow (perdita informazioni per processazione di un numero insufficiente di bit)
    - Un programma assembly viene assemblato in linguaggio macchina, caricato in ram, e assieme ai dati D dai supporti vengono processati dalla CPU dati che portano a dei risultati.

    - Sistemi operativi:
        - isolano utenti dai dettagli del hardware
        - la struttura è a buccia di cipolla
        - ogni livello si appoggia a quello inferiore
            - livello più basso: kernel:
                -gestione delle periferiche (quindi anche driver)
                -gestione della memoria (quindi file system anche)
                -gestione dei processi (nucleo)
        - ogni processo è una coppia di elementi (codice eseguibile, stato del processo)
            - il gestore dei processi del SO controlla la sincronizzazione, sospensione e riattivazione dei processi, che permettono il multitasking (più programmi allo stesso tempo condividono la CPU)
            - gli stati di un processo possono essere:
                -in esecuzione (assegnato al processore)
                -bloccato/in attesa (aspetta un evento I/O esterno per diventare pronto per l'esecuzione)
                -pronto per l'esecuzione (può andare in esecuzione se il gestore dei processi lo decide)

                - il gestore dei processi mantiene lo stato di ogni processo
        - time sharing - tecnica di ripartizione del tempo d'utilizzo della CPU tra tutti i processi che se la contendono, cioè che sono allo stesso tempo in esecuzione. Di solito qualche millisecondo. Così il programma/processo/utente hanno l'illusione di poter disporre singolarmente della CPU. Qui entra in gioco anche le priorità.
            - coordinamento sequenziale - la terminazione di un processo invoca l'attivazione di un altro
            - competizione - due processi vogliono accedere simultaneamente alla medesima risorsa.
        - la CPU passa da un processo all'altro quando riceve un segnale di interrupt.
        - Il controllo che porta al multitasking avviene tramite priorità e interruzioni. Entra in gioco lo scheduler che esegue una foto del contenuto dei registri della CPU mentre sta eseguendo il PR, in particolare i registri P, IR, di calcolo, etc, memorizzando il tutto nella RAM. Quando PR torna in esecuzione la foto viene usata per riportare la CPU allo stesso stato prima del blocco.

        - Una parte del RAM è per il SO. Il programma che carica in ram i programmi si chiama "Loader". Ci sono ovviamente limiti al caricamento in RAM dei programmi, e il gestore della memoria deve essere in grado di suddividere la RAM per assegnarne porzioni a ciascun programma.
            - i meccanismi di suddivisione della memoria:
                - segmentazione - suddivisa in segmenti di lunghezza variabile, occupati o liberi. I "frammenti di memoria" sono zone di memoria libera tra due segmenti successivi occupati da programmi. Il gestore riduce la frammentazione con una politica "best-fit", allocando ciascun programma nel più piccolo segmento libero di memoria (cioè frammento) che lo contiene.
                - paginazione - pagina di zona contigua di memoria di grandezza fissata in modo che la ram contenga 2^q di pagine. I programmi vengono suddivisi in pagine ed allocati in un numero intero di pagine non necessariamente contigue. Non tutte le pagine sono contemporaneamente in RAM.

                - spesso sono applicate contemporaneamente.

            - I segmenti di memoria hanno lunghezza variabile, le pagine di memoria hanno lunghezza fissa.
        
        - Catena di programmazione:
            - compilatore - trasforma un modulo di programma sorgente in un modulo di programma in linguaggio macchina.
            - linker - trasforma diversi moduli oggetto in un unico programma eseguibile.
            - loader - carica il programma eseguibile in memoria.

        - Gestore della memoria offre al programma la visione di una memoria virtuale diversa da quella fisica. I programmi in linguaggio macchina fanno riferimento a degli indirizzi logici o virtuali di memoria e non ad indirizzi assoluti (cioè fisici). Il caricatore deve ricollocare di continuo indirizzi logici in indirizzi fisici.
           - Processori a 32 bit = 4gb di ram / 64bit = 16 millioni di terabytes. Quindi la memoria virtuale massima su un 32bit è di 4GB. Su un 64bit possiamo avere più memoria virtuale che fisicamente disponibile.
            - Possiamo usare la memoria secondaria come fosse RAM virtuale (swap su disco) con ovvi svantaggi e vantaggi.

        - Driver gestiscono I/O, e sono software. 

        - File System si occupa di fornire programmi per accedere e gestire i file. Rendendo invisibile la struttura fisica della memoria di massa e ottimizzando in base alla necessità l'occupazione dei dati.
            - Ha un'Organizzazione gerarchica. I file diventano unità logica di informazione, con tanto di identificatore, dettagli di creazione, modifica, dimensione, e posizione effettiva nella memoria di massa (oltre a diritti di accesso, ecc). Le estensioni permettono al SO di riconoscere il tipo di software da usare con un singolo file. 
            - Una directory è un insieme di file e altre directory, organizzati ad albero. Il percorso dei file permette di identificare la posizione in questa struttura gerarchica.

        - Vi sono vari OS disponibili, portatili e non, alcuni anche estremamente specifici come per il mainframe IBM AS400

- Misura della complessità nel caso peggiore e nel caso medio, notazione O-grande. Il paradigma ricorsivo.
    - si può rivelare il tempo con "time()"
    - si contano le operazioni onerose dal punto di vista del tempo di esecuzione:
        - un ciclo è un fattore moltiplicativo (nOperazioni*cicli)
        - si contano come operazioni SOLO gli accessi in lettura o scrittura a elementi della lista, ipotizzando come trascurabile il tempo delle altre operazioni di assegnazione: 
            ```python
            >>> temp = values[minPos]
            >>> values[minPos]=values[i]
            >>> values[i]=temp
                # 4 accessi a liste, 4 operazioni
            ```
    - prestazioni algoritmi di ordinamento:
        - selezione = O(n^2)
        - inserimento = O(n^2) nel caso peggiore, O(n) nel migliore
        - fusione = O(n log n)




- Algoritmi di ordinamento: selezione, inserzione, fusione.
    - selezione:
        - si cerca l'elemento minore di una lista, lo si posiziona all'inizio della lista scambiandolo con l'elemento già presente, e poi si prosegue a rianalizzare la lista rimanente, fino alla fine
    - **inserzione**:
        1. la sottolista di lunghezza unitaria della lista (primo elemento) è ordinata
        2. estendi verso destra la parte ordinata
        3. sposti il nuovo elemento verso sinistra finché non si trova nella sua posizione corretta (elemento in i più grande di i-1, più piccolo di i+1)

        - ***In Python***:
            ```python
            loop lungo quanto la lista (fino a len(lista))
                salvo il valore in i
                j=i
                mentre j>0, e lista[j-1]>valore in i
                    lista[j]=lista[j-1]
                    j=j-1
                lista[j]=valore in i```
    - **fusione**:
        - "dividi et impera"
        - si spezza la lista finché si ottengono elementi singoli (n liste da 1 elemento). E lo si fa in modo ricorsivo.
            - caso base: >= 1 elemento nella lista.
            - resto casi: la lista si divide in due, si richiama mergeSort sulle due liste. 
            - quando si hanno due list di un elemento l'una, si reintegra ina una sola lista, mettendo il più piccolo elemento/i all'inizio.

- Da studiare da Slide:
    - ***Strutture*** per la memorizzazione di dati: tipo di dato astratto; array.
    - ***Liste, pile e code***: realizzazione mediante un array o una catena di celle.
    - ***Ricerca*** di un elemento ***in un array*** e in una lista.
    - Ricerca per ***bisezione*** in un array ordinato.
    - ***Tabelle e dizionari***: semplice realizzazione mediante un array o una lista.
    - ***Alberi binari*** di ricerca e ***heap*** (code prioritarie).
