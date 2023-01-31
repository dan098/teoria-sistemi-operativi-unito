import random

questions = {
    #capitolo 1
    "legge di Amdahl": "le prestazioni di un processore N-core aumentano meno che linearmente rispetto al numero di core disponibili",
    "Interrupt": ": sono eventi di natura hardware, che si \
manifestano come segnali elettrici inviati da qualsiasi \
elemento dell’architettura del computer che richieda \
l’intervento del SO.",
    "Eccezioni": "sono eventi di natura software, cioè causati dal \
programma in esecuzione, e devono essere gestiti dal SO e si distinguono in trap e system calls",
    "come fa il sistema operativo a mantenere costantemente il controllo della macchina" : "utilizzando un processo chiamato \"schedulazione\". La schedulazione è la funzione del sistema operativo che determina quale processo o attività deve essere eseguita successivamente dalla CPU.",
    "interazione tra i dispositivi di I/O e il SO" : "Ogni dispositivo di I/O è controllato da un apposito componente hardware detto controller, un piccolo processore con una memoria detta buffer, Il SO interagisce con il controller attraverso un software apposito noto come driver del dispositivo",
    "multi-tasking e time sharing" : "se non la sai sei un clown, comunque:multitasking avere sempre un processo running per la massima utilizzazione della CPU//timesharing distribuire l’uso della CPU fra i processi a intervalli prefissati.",
    "compiti del SO (sono 5)" : "1.gestire processi e thread e attribuire appropriamente cpu usage a ciascuno\n2.cpu scheduling\n3.permettere sincronizzazione dei processi ed evitare deadlock\n4.gestire memoria centrale e virtuale\n5.implementare il file system e gestire le informazioni salvate in memoria secondaria",
    #capitolo 3
    "stati di un processo" : "new, ready to run, running, waiting, terminated",
    "che significato ha eliminare l’arco “interrupt” o “wait”" : "un processo che viene messo in stato running non esce finchè non ha terminato la sua esecuzione (quanto di tempo inutile), inoltre per esempio in caso di operazioni i/o farebbe busy waiting sprecando tempo di esecuzione che potrebbe essere attribiuti ad altri processi nel frattempo",
    "come funziona il context switch" : "il SO: 1. riprende il controllo della cpu\n2. salva lo stato corrente del processo rimosso copiando i registri nel suo PCB (Process Control Block)\n3. scrivere nel Program Counter e negli altri registri della CPU i valori del PCB del nuovo processo",
    "overhead/dispatch latency" : "tempo sprecato per l'esecuzione del context switch",
    #capitolo 4
    "perchè esistono i thread/task e cosa sono" : "sono processi che possono condividere uno spazio di indirizzamento per ridurre i context switch e operare quindi sugli stessi dati contemporaneamente",
    #capitolo 5
    "cosa si intende per starvation e qual è la soluzione a tale problematica" : "Si dice che va in starvation un processo che non verrà mai scelto dallo scheduler, per risolvere questo problema si usa un meccanismo di aging",
    "scheduling Round Robin" : "Ogni processo ha a disposizione una certa quantità di tempo di CPU, chiamata quanto di tempo, risolve il problema della starvation se non-preemptive",
    "classi di processi per scheduling a code multiple" : "foreground (interattivi, ad esempio un editor), background (non interagiscono con l’utente), batch (la loro esecuzione può essere differita)",
    "Turnaround time" : "tempo medio di completamento di un processo in uno specifico sistema di scheduling (da minimizzare riducendo il tempo di attesa di ogni processo)\n\
esempio turnaround medio con FCFS:  sum(completamento(i-1) + burst(i) - arrival(i)) / nProcessi",
    "Waiting time" : "tempo totale passato in ready queue da un processo",
    #capitolo 9
    "tipi di binding degli indirizzi" : "il binding degli indirizzi può avvenire:\nin fase di compilazione - viene generato codice assoluto (gestione rigida)\n\
in fase di caricamento - viene generato codice staticamente rilocabile dal compilazione con indirizzi relativi che fanno riferimento ad un ipotetico 0 virtuale\n\
in fase di esecuzione - viene generato codice dinamicamente rilocabile e quindi il codice in esecuzione fa sempre e solo riferimento a indirizzi relativi (binding dinamico)",
    "come funzione il binding dinamico" : "gli indirizzi relativi delle istruzioni in esecuzione vengono trasformati in assoluti con un apposito registro di rilocazione che contiene l'indirizzo di partenza in RAM del programma in esecuzione dalla MMU(memory management unit)"
    "differenze tra librerie statiche e dinamiche" : "Le librerie statiche sono incorporate nell'eseguibile del programma durante la compilazione, mentre le librerie dinamiche possono essere caricate dinamicamente in memoria durante l'esecuzione del programma. Le librerie dinamiche possono essere condivise da più programmi, risparmiando spazio in memoria, ma richiedono un meccanismo di linking dinamico per essere caricate al momento opportuno, inoltre aggiornamenti alle librerie dinamiche non richiedono la ricompilazione dei programmi",
    "come viene protetta la memoria primaria con l'allocazione contigua" : "tramite un registro limite che viene usato per verificare che l'indirizzo logico sia minore al registro e quindi il programma non possa andare a toccare aree di memoria che non gli appartengono",
    "svantaggi allocazione a partizioni multiple fisse in memoria primaria" : "grado di multiprogrammazione limitato al numero di partizioni previste, frammentazione interna ed esterna, inoltre il singolo processo ha uno spazio di indirizzamento limitato alla dimensione massima della partizione"
    
}

question_list = list(questions.keys())
random.shuffle(question_list)

for question in question_list:
    input("\n"+question)
    print(questions[question])
