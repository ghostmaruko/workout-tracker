from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configurazione del database SQLite 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///workouts.db"
db = SQLAlchemy(app)

# Definizione del modello Workout (è la tabella del database che conterrà i dati degli allenamenti)
class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(20), nullable=False)
    data = db.Column(db.String(20))

    # Campi corsa (nullable perché vuoti se categoria è "palestra")
    tipo_corsa = db.Column(db.String(20), nullable=True)
    distanza_km = db.Column(db.Float, nullable=True)
    tempo_minuti = db.Column(db.Float, nullable=True)
    passo_min_per_km = db.Column(db.Float, nullable=True)
    frequenza_cardiaca_media = db.Column(db.Integer, nullable=True)

    # Campi palestra (nullable perché vuoti se categoria è "corsa")
    esercizio = db.Column(db.String(100), nullable=True)
    serie = db.Column(db.Integer, nullable=True)
    ripetizioni = db.Column(db.Integer, nullable=True)
    peso = db.Column(db.Float, nullable=True)

    # Metodo per convertire l'oggetto Workout in un dizionario (utile per la serializzazione JSON)
    def to_dict(self):
        return {
            "id": self.id,
            "categoria": self.categoria,
            "data": self.data,
            "tipo_corsa": self.tipo_corsa,
            "distanza_km": self.distanza_km,
            "tempo_minuti": self.tempo_minuti,
            "passo_min_per_km": self.passo_min_per_km,
            "frequenza_cardiaca_media": self.frequenza_cardiaca_media,
            "esercizio": self.esercizio,
            "serie": self.serie,
            "ripetizioni": self.ripetizioni,
            "peso": self.peso,
        }


@app.route("/")
def home():
    return "Workout Tracker è vivo!"


@app.route("/api/workouts", methods=["GET"])
def get_workouts():
    # Recupera tutti gli allenamenti dal database e li restituisce come JSON
    tutti = Workout.query.all()
    return jsonify([w.to_dict() for w in tutti])


@app.route("/api/workouts", methods=["POST"])
def add_workout():
    data = request.get_json()
    categoria = data.get("categoria")

    if categoria not in ("corsa", "palestra"):
        return jsonify({"errore": "categoria deve essere 'corsa' o 'palestra'"}), 400

    if categoria == "corsa":
        campi_richiesti = ["tipo_corsa", "distanza_km", "tempo_minuti"]
        mancanti = [c for c in campi_richiesti if c not in data]
        if mancanti:
            return jsonify({"errore": f"campi mancanti per corsa: {mancanti}"}), 400

        distanza_km = data["distanza_km"]
        tempo_minuti = data["tempo_minuti"]

        if distanza_km <= 0 or tempo_minuti <= 0:
            return jsonify({"errore": "distanza_km e tempo_minuti devono essere maggiori di zero"}), 400

        passo = round(tempo_minuti / distanza_km, 2)

        nuovo = Workout(
            categoria="corsa",
            tipo_corsa=data["tipo_corsa"],
            distanza_km=distanza_km,
            tempo_minuti=tempo_minuti,
            passo_min_per_km=passo,
            frequenza_cardiaca_media=data.get("frequenza_cardiaca_media"),
            data=data.get("data"),
        )

    else:  # palestra
        campi_richiesti = ["esercizio", "serie", "ripetizioni", "peso"]
        mancanti = [c for c in campi_richiesti if c not in data]
        if mancanti:
            return jsonify({"errore": f"campi mancanti per palestra: {mancanti}"}), 400

        nuovo = Workout(
            categoria="palestra",
            esercizio=data["esercizio"],
            serie=data["serie"],
            ripetizioni=data["ripetizioni"],
            peso=data["peso"],
            data=data.get("data"),
        )

    # Aggiunge il nuovo allenamento al database
    db.session.add(nuovo)
    # Commit delle modifiche al database
    db.session.commit()

    return jsonify(nuovo.to_dict()), 201


if __name__ == "__main__":
    # Crea le tabelle del database se non esistono già 
    with app.app_context():
        db.create_all()
    app.run(debug=True)