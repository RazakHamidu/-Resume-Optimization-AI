# Resume Optimization AI

**Problema**: Quando si inviano candidature a più aziende, è fondamentale che il curriculum sia in linea con i requisiti di ciascuna posizione lavorativa. Tuttavia, personalizzare il CV per ogni candidatura può essere un processo lungo e noioso, soprattutto per chi deve inviare molte candidature in poco tempo.

**Soluzione**: Resume Optimization AI è un'applicazione che utilizza modelli di AI per personalizzare automaticamente il curriculum. L'app prende in input un curriculum e una descrizione del lavoro, e genera un CV ottimizzato che evidenzia le competenze e le esperienze più rilevanti per la posizione desiderata.


## Caratteristiche

-   **Caricamento Curriculum**: Carica il tuo curriculum esistente in formato PDF.
-   **Inserimento Descrizione Lavoro**: Inserisci le descrizioni di lavoro direttamente nell'applicazione.
-   **Ottimizzazione con AI**: Utilizza un modello di AI generativa (modello Gemini) per personalizzare i curriculum.
-   **Download Curriculum**: Scarica il nuovo curriculum personalizzato.

----------

## Installazione

### Prerequisiti

Assicurati di avere installato:

-   Python 3.8+
-   pip (gestore pacchetti Python)

### Procedura di Installazione

1.  Clona il repository:
    
    ```bash
    git clone https://github.com/your-username/resume-optimization.git
    cd resume-optimization
    
    ```
    
2.  Crea un ambiente virtuale:
    
    ```bash
    python -m venv venv
    source venv/bin/activate   # Su Windows: venv\Scripts\activate
    
    ```
    
3.  Installa le dipendenze:
    
    ```bash
    pip install -r requirements.txt
    
    ```
4. Scarica wkhtmltopdf
	5. 1. Vai al sito ufficiale di **wkhtmltopdf**:  
   [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)

2. Seleziona la versione compatibile con il tuo sistema operativo:
   - **Windows**: Scarica il file `.exe` (versione stabile consigliata).
   - **macOS**: Scarica il pacchetto `.dmg`.
   - **Linux**: Puoi scaricare il pacchetto `.deb` o `.rpm`.

**Installazione per Sistema Operativo**

### **Per Windows**
1. Esegui il file `.exe` scaricato.
2. Segui le istruzioni della procedura guidata di installazione.
3. Durante l'installazione:
   - Assicurati di selezionare l'opzione per aggiungere wkhtmltopdf al **PATH** di sistema.
4. Al termine, verifica l'installazione aprendo il prompt dei comandi (CMD) e digitando:
   ```bash
   wkhtmltopdf --version
   ```
   Dovresti vedere la versione installata di wkhtmltopdf.

---

### **Per macOS**
1. Apri il file `.dmg` scaricato.
2. Trascina l'app wkhtmltopdf nella cartella delle Applicazioni.
3. Aggiungi wkhtmltopdf al tuo PATH:
   - Modifica il file `~/.zshrc` (o `~/.bash_profile` se usi bash) e aggiungi:
     ```bash
     export PATH="/Applications/wkhtmltopdf.app/Contents/MacOS:$PATH"
     ```
   - Salva il file e ricarica la configurazione:
     ```bash
     source ~/.zshrc
     ```
4. Verifica l'installazione eseguendo:
   ```bash
   wkhtmltopdf --version
   ```

---

### **Per Linux**
#### Ubuntu/Debian:
1. Scarica il pacchetto `.deb` dal sito ufficiale.
2. Installa il pacchetto usando:
   ```bash
   sudo dpkg -i wkhtmltox_*.deb
   ```
3. Risolvi eventuali dipendenze mancanti:
   ```bash
   sudo apt-get install -f
   ```
4. Verifica l'installazione:
   ```bash
   wkhtmltopdf --version
   ```
---
    
6.  Configura le variabili d'ambiente:
    
    -   Crea un file `.env` nella directory principale.
    -   Aggiungi la tua chiave API per il modello Gemini:
        
        ```
        GEMINI_API_KEY=la_tua_chiave_api
        
        ```
        
7.  Avvia l'applicazione:
    
    ```bash
    streamlit run main.py
    
    ```
    

----------

## Utilizzo

1.  **Carica il Curriculum**:
    
    -   Carica il tuo curriculum in formato PDF utilizzando l'apposito uploader.
2.  **Inserisci Descrizione del Lavoro**:
    
    -   Incolla la descrizione del lavoro nell'area di testo fornita.
3.  **Ottimizza il Curriculum**:
    
    -   Clicca sul pulsante di caricamento per elaborare il curriculum.
    -   Visualizza il curriculum aggiornato in formato Markdown nell'interfaccia.
4.  **Scarica il Curriculum**:
    
    -   Scarica il curriculum personalizzato in formato PDF.

----------

## Struttura dei File

```
resume-optimization/
|── __pycache__/         # File di cache Python
|── .env                # Variabili d'ambiente
|── .gitignore          # File per ignorare determinati file in Git
|── main.py             # Script principale dell'applicazione
|── requirements.txt    # Elenco delle dipendenze

```

----------

## Tecnologie Utilizzate

-   **Python**: Linguaggio di programmazione principale.
-   **Streamlit**: Framework per applicazioni web interattive.
-   **pdfplumber**: Per estrarre testo dai file PDF.
-   **markdown**: Per convertire Markdown in HTML.
-   **pdfkit**: Per convertire HTML in PDF.
-   **Gemini**: Modello AI per la generazione di contenuti.

----------

----------

## Licenza

Questo progetto è concesso in licenza sotto la Licenza MIT. Consulta il file `LICENSE` per maggiori dettagli.
