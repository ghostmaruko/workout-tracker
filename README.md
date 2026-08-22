# Workout Tracker

API per tracciare allenamenti di corsa e palestra, costruita come progetto di apprendimento per QA Automation Engineering. In preparazione per la Maratona di Berlino 2026.

## Stack

- **Backend**: Flask (Python)
- **Database**: SQLite + SQLAlchemy
- **Test**: pytest, con test client di Flask (database in memoria, isolato dai dati reali)

## Modello dati

Un allenamento può essere di due categorie:

**Corsa**: `tipo_corsa` (long_run / ripetute / recupero / tempo_run), `distanza_km`, `tempo_minuti`, `passo_min_per_km` (calcolato automaticamente), `frequenza_cardiaca_media` (opzionale)

**Palestra**: `esercizio`, `serie`, `ripetizioni`, `peso`

## Endpoint

- `GET /api/workouts` — restituisce tutti gli allenamenti
- `POST /api/workouts` — crea un nuovo allenamento (valida i campi obbligatori in base alla categoria)

## Setup locale

\`\`\`bash
python -m venv venv
venv\Scripts\activate       # Windows
pip install -r requirements.txt
py app.py
\`\`\`

Il server parte su `http://127.0.0.1:5000`.

## Eseguire i test

\`\`\`bash
pytest
\`\`\`

I test usano un database SQLite in memoria, separato da `workouts.db` — nessun dato reale viene toccato.

## Stato del progetto / prossimi step

- [x] API Flask con validazione per categoria
- [x] Persistenza SQLite
- [x] Repository Git + `.gitignore`
- [x] Test API con pytest (test client, database isolato)
- [ ] Frontend HTML con form (necessario per i test UI)
- [ ] Test UI con Playwright
- [ ] CI/CD con GitHub Actions
- [ ] Deploy su Raspberry Pi
- [ ] Integrazione Strava (fase avanzata, con mocking delle chiamate esterne nei test)