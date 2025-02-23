# Alcuni esercizi di programmazione e la relativa possibile soluzione

<details>
<summary>Bateri.txt</summary>
<br>

 	"""
	Si implementi un programma che simula, in una griglia quadrata 2D di L per L celle (non è necessario visualizzarla),
	l'interazione tra cellule batteriche e cellule del sistema immunitario.
	La griglia è occupata in una certa percentuale da cellule batteriche
	e in un'altra percentuale da cellule del sistema immunitario (percentuali date in input dall'utente).
	Le celle rimanenti sono da considerare "libere".
	
	Il tempo viene simulato attravero un ciclo for e una variabile di iterazione t
	per un numero di iterazioni t_max fornito dall'utente.
	
	Ogni iterazione è divisa in due fasi. Quando la fase 1 è completata, inizia la fase 2.
	FASE 1:
	Ogni cellula (batterica e del sistema immunitario) si sposta di posizione in una casella nel suo intorno
	a una distanza massima di raggio rmov fornito dall'utente. Se nel raggio di azione non ci sono posizioni libere
	la cellula non si muove.
	FASE 2:
	Ogni cellula batterica che abbia raggiunto volume >= 2 si divide (vd. DIVISIONE CELLULARE),
	altrimenti aumenta il suo volume del 30%.
	A questo punto, se una cellula batterica ha come vicine delle cellule del sistema immunitario, viene attaccata
	a turno da ciascuna delle vicine con una probabilità di morire del 20%. Se muore ovviamente non ci sono ulteriori attacchi
	Se la cellula del sistema immunitario vince contro il batterio, il batterio scompare dalla griglia
	e al suo posto appare una nuova cellula del sistema immunitario.
	Dopo 9 attacchi (con o senza successo) la cellula del sistema immunitario muore.
	
	DIVISIONE CELLULARE
	Le cellule batteriche, quando nascono, hanno volume iniziale = 1 e, quando raggungono volume >= 2 si dividono
	in due cellule figlie ciascuna di volume 1. Una resta nella posizione della cellula genitore,
	l'altra compare nella griglia in una posizione random che non sia però occupata
	da cellule batteriche o del sistema immunitario.
	Se non ci sono più posizioni libere la seconda cellula non compare nella griglia.
	La seconda cellula non subisce attacchi nella iterazione in cui è stata creata.
	
	
	Il codice seguente implementa il programma BACTvsIS.py che fa uso di due classi: Batterio e IScell,
	entrambe figlie della superclasse Cellula.
	Il programma salva in un file, ad ogni iterazione, il numero di cellule batteriche e il numero di cellule
	del sistema immunitario presenti nel sistema.
	Implementare il codice che definisce le tre classi in modo che il programma funzioni correttamente. 
	il codice implementato va salvato nel file cellule.py
	"""
	
	import random
	from cellule import Cellula, Batterio, IScell
	
	#inizializza la griglia 2D L per L con 0 in corrispondenza di cella vuota, e oggetti di tipo Batterio o IScell altrimenti
	# con probabilità specificate dai parametri perc_batt e perc_is, rispettivamente
	# @L lato griglia quadrata
	# @perc_batt % batteri iniziale (un numero tra 0 e 1)
	# @perc_is % cellule IS iniziale (un numero tra 0 e 1)
	def gridinit(L = 20, perc_is = 0.1, perc_batt = 0.01):
	    grid = []  
	    new = []
	    for i in range(L):
		for j in range(L):
		    if random.random() <= perc_is:
			new.append(IScell(i,j))
		    elif random.random() <= perc_batt:
			new.append(Batterio(i,j))
		    else:
			new.append(Cellula.EMPTY)
		grid.append(new)
		new = []
	    return (grid)
	
	# itera t_max volte un processo di
	#@ 1) movimento di tutte le cellule batteriche e IS
	#@ 2) azione delle cellule batteriche (dividersi, morire, crescere) e rispettiva azione cellule IS se queste attaccano
	def itera(t_max, grid, rmov, filename):
	    L = len(grid)
	    outfile = open(filename, "w")
	    for t in range(t_max):
		print(t, "\t", Batterio.contaBatteri, "\t", IScell.contaIS)
		outfile.write(str(Batterio.contaBatteri)+"\t"+str(IScell.contaIS)+"\n")
		for i in range(L):
		    for j in range(L):
			if (grid[i][j]!=Cellula.EMPTY):
			    grid[i][j].move(grid, rmov)
		for i in range(L):
		    for j in range(L):
			if (grid[i][j]!=Cellula.EMPTY):
			    grid[i][j].act(grid)
	    outfile.close()     
	
	
	def main():
	    L = int(input("Input size of square 2D grid. It must be an int: "))
	    perc_is = float(input("Input % of immune system (IS) cells at time 0 (a number between 0 and 1): "))
	    perc_batt = float(input("Input % of bacteria cells at time 0(a number between 0 and 1): "))
	    griglia = gridinit(L, perc_is, perc_batt)    
	    filename = input("Input the name of the output file: ")
	    t_max = int(input("Input number of iterations. It must be an int: "))
	    raggioMov = int(input("Input max movement distance r. It must be an int: "))
	    itera(t_max = t_max, grid = griglia, rmov = raggioMov, filename = filename)
	  
	
	
	main() 
 
</details>

<details>
<summary>Batteri_soluzione.txt</summary>
<br>

	"""
	Cellula è la superclasse di Batterio e IScell. Definirà quindi le proprietà e i metodi di una cellula "generica".
	Dal testo si evince che la classe Cellula definirà:
	• una posizione x,y della cellula nella griglia (vedi i costruttori IScell(i,j) e Batterio(i,j))
	• una variabile di classe Cellula.EMPTY per indicare le celle vuote nella griglia
	• un metodo move(grid, r) per "muovere" la cellula nella griglia grid in un intorno di raggio r
	• un metodo (che chiameremo die()) per simulare la morte della cellula
	• una variabile di esemplare (che chiameremo _acted) per memorizzare se la cellula è già stata spostata nell’iterazione corrente 
	
	Riguardo il metodo act(grid), questo è un metodo che deve essere a
	disposizione di ogni oggetto Cellula, ma il cui comportamento è dipendente
	dal tipo di cellula.
	Di conseguenza il metodo act(grid) si definisce solo nelle classi Batterio e
	IScell.
	"""
	
	import random
	
	class Cellula():
	
	    EMPTY = 0 # è una variabile costante che ci serve a memorizzare il valore 0 (cella "vuota" nella griglia)
	
	    ## costruttore
	    #@param x: coordinata x della cellula
	    #@param y: coordinata y della cellula
	    #@param acted: parametro inizializzato di default a False per indicare che, se la cellula è appena nata, non ha ancora agito
	    def __init__(self,x,y,acted=False):
	        self._x = x
	        self._y = y
	        self._acted = acted
	
	    ## conta i vicini (max distanza r) di un certo tipo e restituisce le coordinate della posizione
	    #@param griglia una lista di liste in cui ogni elemento è 0 (celle vuota) oppure un oggetto di tipo Batterio o di tipo IScell
	    #@param r un intero che indica entro che raggio attorno alla posizione corrente cercare i vicini
	    #@param tipo è il nome di una classe: Cellula, Batterio, IScell... o int (se cerco le celle vuote contenenti il numero 0, che è un oggetto di tipo int)
	    def getvicini(self, griglia, r, tipo):
	        vicini = []
	        L = len(griglia)
	        min_x = max(0, self._x-r)
	        max_x = min(L-1, self._x+r)
	        min_y = max(0, self._y-r)
	        max_y = min(L-1, self._y+r)
	        for i in range(min_x, max_x+1):
	            for j in range(min_y, max_y+1):
	                if isinstance(griglia[i][j], tipo):
	                    vicini.append((i,j))
	        return vicini
	      
	    ## il metodo move() serve per "muovere" la cellula nella griglia grid in una posizione
	    #  "vuota" scelta a caso in un intorno di raggio r
	    # Attenzione! E' necessario tenere traccia di quali cellule sono già state spostate nell’iterazione
	    # corrente, così da sapere quali non rispostare mentre si scorre la griglia
	    #@param griglia una lista di liste in cui ogni elemento è 0 (celle vuota) oppure un oggetto di tipo Batterio o di tipo IScell
	    #@param r un intero che indica entro che raggio la cellula si può muovere
	    def move(self, griglia, r):
	        if self._acted == False:
	            posizioni = self.getvicini(griglia, r, tipo = int) #cerco le posizioni vuote in cui posso muovermi
	            if len(posizioni)>0:
	                (newx,newy) = random.choice(posizioni)
	                oldx = self._x
	                oldy = self._y
	                self._x = newx
	                self._y = newy
	                griglia[newx][newy] = self
	                griglia[oldx][oldy] = Cellula.EMPTY
	                if (newy > oldy) or ((newy == oldy) and (newx > oldx)): #metto a True _acted se la posizione nella griglia deve ancora essere visitata (non voglio muovere 2 volte la cellula)
	                    self._acted == True
	        else:
	            self._acted = False  #resetto a False per il prossimo giro
	       
	    ##il metodo die() serve a simulare la morte della cellula
	    #@param griglia una lista di liste in cui ogni elemento è 0 (celle vuota) oppure un oggetto di tipo Batterio o di tipo IScell
	    def die(self, griglia):
	        griglia[self._x][self._y] = Cellula.EMPTY
	 
	    ##il metodo getpos() restituisce la posizione della cellula
	    #@return la tupla (self._x,self._y) con la posizione della cellula
	    def getpos(self):
	        return(self._x,self._y)
	
	    ##il metodo getacted() restituisce il valore di self._acted
	    #@return un Booleano (True o False) corrispondente al valore di self._acted
	    def getacted(self):
	        return(self._acted)
	
	    def setacted(self,v):
	        self._acted = v
	
	
	
	'''IScell è una sottoclasse di Cellula, erediterà quindi gli
	attributi e i metodi in essa definiti.
	Inoltre, la classe IScell definirà:
	• un variabile _numattacks per tenere traccia del numero di
	attacchi effettuati dalla cellula del sistema immunitario
	• una variabile di classe IScell.contaIS per indicare il numero
	totale di cellule del sistema immunitario nella griglia
	• una variabile di classe IScell.MAX_ATTACKS per indicare il
	numero massimo di attacchi da effettuare prima di morire
	• un metodo act(grid) che, in caso di raggiungimento del
	numero massimo di attacchi, faccia morire la cellula del
	sistema immunitario
	• un metodo attack() che aggiorna il numero di attacchi effettuato dalla cellula
	• il distruttore __del__() che si prende il compito di aggiornare il contatore della classe
	
	'''
	
	class IScell(Cellula):
	    ## variabili di classe IScell
	    ## contaIS (numero totale di cellule del sistema immunitario nella griglia)
	    ## MAX_ATTACKS (numero massimo di attacchi da effettuare prima di morire (9))
	
	
	    contaIS = 0
	    MAX_ATTACKS = 9
	
	    ## costruttore
	    #@param x: coordinata x della cellula
	    #@param y: coordinata y della cellula
	    #@param acted: parametro inizializzato di default a False per indicare che, se la cellula è appena nata, non ha ancora agito
	    #In aggiunta il costruttore deve inizializzare la variabile self._numattacks e aggiornare le variabili di classe se necessario
	    def __init__(self,x,y,acted=False):
	        super().__init__(x,y,acted)
	        self._numattacks = 0
	        IScell.contaIS = IScell.contaIS + 1
	
	    ## il un metodo act() in caso di raggiungimento del
	    #  numero massimo di attacchi, fa morire la cellula
	    #@param griglia una lista di liste in cui ogni elemento è 0 (celle vuota) oppure un oggetto di tipo Batterio o di tipo IScell  
	    def act(self, griglia):
	        if self._numattacks == IScell.MAX_ATTACKS:
	            self.die(griglia)
	
	    ## il metodo attack() aggiorna il numero di attacchi
	    def attack(self):
	        self._numattacks = self._numattacks + 1
	
	    ## questo è il distruttore... che si prende il compito di aggiornare il contatore della classe
	    def __del__(self):
	        IScell.contaIS = IScell.contaIS - 1
	
	
	
	'''
	Batterio è una sottoclasse di Cellula, erediterà quindi gli attributi e i metodi in essa
	definiti.
	Inoltre la classe Batterio definirà:
	• una variabile _vol per tenere traccia del volume della cellula batterica
	• una variabile di classe Batterio.contaBatteri per indicare il numero totale di cellule
	batteriche nella griglia
	• una variabile di classe Batterio.PERC_GROWTH per definire il tasso di crescita (0.3)
	del batterio
	• una variabile di classe Batterio.VOLDIV per definire il volume oltre il quale si esegue
	la duplicazione (2)
	• una variabile di classe Batterio.PROB_DIE per definire la probabilità di morte in
	caso di attacco di una cellula del sistema immunitario (0.2)
	• un metodo growth() che simula la crescita (di volume) della cellula batterica della percentuale PERC_GROWTH
	• un metodo divide() che simula la duplicazione cellulare facendo comparire una nuova cellula in una posizione a caso tra quelle "vuote"
	• un metodo act(grid) che: i) esegue l’eventuale crescita/duplicazione; ii) simula l’attacco di eventuali cellule del sistema immunitario nelle vicinanze
	• il distruttore __del__() che si prende il compito di aggiornare il contatore della classe
	'''
	
	class Batterio(Cellula):
	    ##variabili di classe Batterio
	    ##contaBatteri (numero totale di cellule batteriche nella griglia)
	    ##PERC_GROWTH (tasso di crescita (0.3))
	    ##VOLDIV (volume oltre il quale si esegue la duplicazione (2))
	    ##PROB_DIE (probabilità di morte in caso di attacco di una cellula del sistema immunitario (0.2))
	    contaBatteri = 0
	    PERC_GROWTH = 0.3
	    VOLDIV = 2
	    PROB_DIE = 0.2
	  
	    ## costruttore
	    #@param x: coordinata x della cellula
	    #@param y: coordinata y della cellula
	    #@param acted: parametro inizializzato di default a False per indicare che, se la cellula è appena nata, non ha ancora agito
	    #@param vol: parametro inizializzato di default a 1 per indicare il volume iniziale della cellula
	    #In aggiunta il costruttore deve inizializzare la variabile self._numattacks e aggiornare le variabili di classe se necessario
	    def __init__(self, x, y, acted = False, vol = 1):
	        super().__init__(x,y,acted)
	        self._vol = vol
	        Batterio.contaBatteri = Batterio.contaBatteri + 1
	    
	    ## il metodo growth() simula la crescita (di volume) della cellula batterica della percentuale PERC_GROWTH
	    def growth(self):
	        self._vol = self._vol*(1 + Batterio.PERC_GROWTH)
	    
	    ## il metodo divide() simula la duplicazione cellulare facendo comparire una nuova cellula in una posizione a caso tra quelle "vuote"
	    ## Sia la nuova che la vecchia cellula avranno volume 1
	    ## La variabile self._acted invece va impostata a False o a True per la cellula
	    ## appena apparsa a seconda della posizione della griglia (da visitare o già visitata all'iterazione corrente)
	    #@param griglia una lista di liste in cui ogni elemento è 0 (celle vuota) oppure un oggetto di tipo Batterio o di tipo IScell  
	    def divide(self, griglia):
	        self._vol = 1 # ogni nuova cellula avrà volume 1
	        posizioni = self.getvicini(griglia, r = len(griglia), tipo = int) #cerco le posizioni vuote in cui possono comparire nuovi batteri
	        (x,y) = self.getpos()
	        if len(posizioni)>0:
	            (newx,newy) = random.choice(posizioni)
	            if (newy > y) or ((newy == y) and (newx > x)): #metto a True _acted se la posizione nella griglia è già stata visitata 
	                griglia[newx][newy] = Batterio(newx, newy, acted = True)
	            else:
	                griglia[newx][newy] = Batterio(newx, newy)
	        
	    ## il metodo act() i) esegue l’eventuale crescita/duplicazione; ii) simula l’attacco di eventuali cellule del sistema immunitario nelle vicinanze
	    #  Prima di tutto controlla che la cella non abbia già agito. Se lo ha fatto resetta self._acted a False per il prossimo giro
	    #  Altrimenti:
	    #  i) se il volume della cellula ha raggiunto la soglia VOLDIV la cellula si divide; altrimenti cresce
	    #  ii) la cellula "cerca" i vicini di tipo IScell, in un intorno di raggio 1.
	    #  Se ne trova, ciascuno di questi vicini attaccherà a turno la cellula batterica con probabilità di vittoria uguale a _PROB_DIE.
	    #  In caso di vittoria del sistema immunitario ovviamente la cellula batterica muore e al suo posto nasce una cellula IScell.
	    #@param griglia una lista di liste in cui ogni elemento è 0 (celle vuota) oppure un oggetto di tipo Batterio o di tipo IScell  
	    def act(self, griglia):
	        if self.getacted() == False:
	            if self._vol >= Batterio.VOLDIV:
	                self.divide(griglia)
	            else:
	                self.growth()
	            (xb,yb) = self.getpos()
	            posizioni = self.getvicini(griglia, r = 1, tipo = IScell)
	            Lp = len(posizioni)
	            if Lp>0:
	                for (x,y) in posizioni:
	                    griglia[x][y].attack()
	                    if random.random() <= Batterio.PROB_DIE:
	                        self.die(griglia)
	                        griglia[xb][yb] = IScell(xb,yb)
	                        break #esco da ciclo for
	        else:
	            self.setacted(False)  #resetto a False per il prossimo giro
	
	
	    ## questo è il distruttore... che si prende il compito di aggiornare il contatore della classe
	    def __del__(self):
	        Batterio.contaBatteri = Batterio.contaBatteri - 1


 
</details>

----

<details>
<summary>How do I dropdown?</summary>
<br>

	
</details>

<details>
<summary>How do I dropdown?</summary>
<br>
This is how you dropdown.
</details>

<details>
<summary>How do I dropdown?</summary>
<br>
This is how you dropdown.
</details>
