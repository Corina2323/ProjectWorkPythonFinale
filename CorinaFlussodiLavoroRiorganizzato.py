Flusso di Lavoro per l'Analisi e la Predizione del Rating Value
Apertura e Ispezione del Dataset
Obiettivo: Comprendere la struttura e i contenuti del dataset.
Caricare il dataset fra_perfumes.csv in Python.
Esaminare la struttura del dataset:
Colonne principali:
Name: Nome del profumo.
Gender: Target del profumo (per uomini, donne, unisex).
Rating Value: Media del rating (valore target da prevedere).
Rating Count: Numero di valutazioni.
Main Accords: Accordi principali del profumo.
Perfumers: Creatori del profumo.
Description: Breve descrizione del profumo.
url: Link al profumo su Fragrantica.
Controllare se tutte le colonne contengono valori coerenti e identificare eventuali problemi, come valori nulli o duplicati.
Pulizia dei Dati
Obiettivo: Garantire che i dati siano di qualità e pronti per l'analisi.
Valori nulli:
Identificare i valori nulli in Rating Value e Rating Count.
Sostituire i valori mancanti:
Per Rating Value: Riempire con la media o la mediana del rating.
Per Rating Count: Riempire con zero o un valore predefinito.
Rimozione dei duplicati:
Identificare ed eliminare eventuali righe duplicate.
Coerenza delle stringhe:
Verificare Main Accords per eventuali errori di formattazione o liste non standard.
Conversione dei dati:
Trasformare Rating Count in numeri interi.
Analisi dei Dati
Obiettivo: Scoprire relazioni significative e ottenere insight dal dataset.
Statistiche descrittive:
Calcolare media, mediana e deviazione standard di Rating Value.
Distribuzioni:
Esaminare la distribuzione di Gender e Main Accords.
Relazioni tra variabili:
Scoprire se alcune categorie di Main Accords influenzano il Rating Value.
Verificare l'effetto di Gender sui rating.
Visualizzazioni:
Creare un istogramma per la distribuzione del Rating Value.
Creare grafici a barre per Gender e Main Accords.
Preprocessing del Dataset
Obiettivo: Preparare i dati per l'addestramento del modello.
Normalizzazione:
Applicare una normalizzazione (se necessaria) per variabili numeriche come Rating Count.
Conversione delle stringhe in numeri:
Trasformare Gender e Main Accords in variabili numeriche usando il one-hot encoding.
Preparazione dei Dati per il Modello
Obiettivo: Separare i dati in variabili predittive e target.
Separazione delle variabili:
Features: Variabili predittive (Gender, Main Accords, Rating Count, ecc.).
Labels: Variabile target (Rating Value).
Suddivisione del dataset:
Dividere il dataset in training set (80%) e test set (20%).
Modello di Machine Learning
Obiettivo: Creare un modello per predire il Rating Value.
Scelta del modello:
Iniziare con un modello semplice, come la regressione lineare.
Addestramento del modello:
Addestrare il modello sui dati del training set.
Predizioni:
Utilizzare il modello per fare predizioni sul test set.
Valutazione del Modello
Obiettivo: Misurare l'efficacia del modello.
Metriche di valutazione:
Calcolare:
Mean Squared Error (MSE): Per misurare l'errore medio quadratico.
R2 Score: Per valutare quanto bene il modello spiega la variabilità dei dati.
Visualizzazioni:
Creare un grafico scatter per confrontare i valori reali e predetti del Rating Value.


Obiettivi Specifici
Analisi dei Dati:
Analizzare i dati per comprendere le distribuzioni, le tendenze e i pattern significativi.
Predizione del Rating Value:
Creare un modello di machine learning per stimare il rating basandosi sulle altre variabili del dataset.

