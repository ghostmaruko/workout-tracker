# Workout Tracker

API e interfaccia web per tracciare allenamenti di corsa e palestra, costruita come progetto di apprendimento per QA Automation Engineering. In preparazione per la Maratona di Berlino 2026.

## Stack

- **Backend**: Flask (Python)
- **Database**: SQLite + SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript vanilla (nessun framework)
- **Test**: pytest (API, con test client di Flask) + Playwright (UI, browser reale)

## Modello dati

Un allenamento può essere di due categorie:

**Corsa**: `tipo_corsa` (long_run / ripetute / recupero / tempo_run), `distanza_km`, `tempo_minuti`, `passo_min_per_km` (calcolato automaticamente), `frequenza_cardiaca_media` (opzionale)

**Palestra**: `esercizio`, `serie`, `ripetizioni`, `peso`

## Endpoint

- `GET /api/workouts` — restituisce tutti gli allenamenti
- `POST /api/workouts` — crea un nuovo allenamento (valida i campi obbligatori in base alla categoria)

## Interfaccia web

La pagina principale (`/`) mostra tre sezioni selezionabili tramite bottoni:
- **Corsa** — elenco degli allenamenti di corsa, più recenti in cima, mostrati come card
- **Palestra** — elenco degli allenamenti di palestra, stesso formato
- **Profilo** — sezione base, in evoluzione

I dati vengono caricati dinamicamente dall'API (`fetch`) al caricamento della pagina, filtrati per categoria e ordinati per data.

## Setup locale

\`\`\`bash
python -m venv venv
venv\Scripts\activate       # Windows
pip install -r requirements.txt
playwright install         # scarica i browser usati dai test UI
py app.py
\`\`\`

Il server parte su `http://127.0.0.1:5000`.

## Eseguire i test

**Test API** (nessun server acceso necessario, usano un database SQLite in memoria isolato da `workouts.db`):

\`\`\`bash
pytest tests/test_api.py
\`\`\`

**Test UI** (richiedono il server Flask acceso in un altro terminale, aprono un browser reale via Playwright):

\`\`\`bash
py app.py                   # in un terminale separato
pytest tests/test_ui.py     # in questo terminale
\`\`\`

Per eseguire tutti i test insieme (con il server acceso):

\`\`\`bash
pytest
\`\`\`

## Stato del progetto / prossimi step

- [x] API Flask con validazione per categoria
- [x] Persistenza SQLite
- [x] Repository Git + `.gitignore`
- [x] Test API con pytest (test client, database isolato)
- [x] Frontend con interfaccia a sezioni, dati dinamici via fetch
- [x] Stile CSS base e componenti (card, stato attivo)
- [x] Test UI con Playwright
- [ ] CI/CD con GitHub Actions
- [ ] Deploy su Raspberry Pi
- [ ] Integrazione Strava (fase avanzata, con mocking delle chiamate esterne nei test)